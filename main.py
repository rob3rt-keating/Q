"""
Author: J. Robert Keating
Date: 7/1/2022
"""
import datetime
import json
import collections
from pathlib import Path
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from typing import List
import sqlite3
from helpers import Question, QuestionBM
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import make_db_from_json, write_to_json_file
from helpers import Bank

BASE_PATH = Path(__file__).resolve().parent

app = FastAPI()
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))
app.mount("/static", StaticFiles(directory=f"{BASE_PATH}/static"), name="static")


# class Bank:
#     """ Queue for cycling through questions"""
#
#     scores = {}
#
#     def __init__(self, ids=None, cmd=''):
#         self._ids = ids
#         self._cmd = cmd
#
#     def get_db_ids(self, cmd, shuffle, limit):
#         conn = sqlite3.connect(f'{BASE_PATH}/questions.db')
#         cursor = conn.execute(cmd)
#         self._ids = [idx[0] for idx in cursor]
#
#         if shuffle is True:
#             random.shuffle(self._ids)
#
#         if limit:
#             self._ids = self._ids[:int(limit)]
#
#         # self._ids = self._ids
#
#     def list_ids(self):
#         return self._ids
#
#     def remove_id(self, value):
#         self._ids.remove(value)
#
#     def get_next(self):
#         if len(self._ids) == 0:
#             return 0
#         val = self._ids[0]
#         self.remove_id(val)
#         return val
#
#     def add_score(self, value):
#         self.scores = self.scores | value
#
#     def get_scores(self):
#         return self.scores


bank = Bank()


@app.get("/")
async def home(request: Request):
    """ landing page"""

    return TEMPLATES.TemplateResponse("index.html", {"request": request})


@app.post("/id")
async def home(request: Request, idx: str = Form(None)):
    """ landing page"""

    if idx is None:
        return

    data = get_questions(idx)

    return TEMPLATES.TemplateResponse(
        "index.html", {"request": request,
                       "data": data[0],
                       "explain": data[0].get('explain'),
                       "explain_url": data[0].get('explain_url'),
                       'notes': data[0]['notes'].split('~') if data[0]['notes'] is not None else '',
                       })


@app.post("/id_get")
async def get_id(request: Request, idx: str = Form(None)):
    """ post - landing page"""

    data = get_questions(idx)

    return json.dumps(data)


@app.get("/id/{idx}")
async def home(request: Request, idx: str):
    """ git question by id landing page"""

    data = get_questions(idx)

    return TEMPLATES.TemplateResponse(
        "index.html", {"request": request,
                       "data": data[0],
                       "explain": data[0].get('explain'),
                       "explain_url": data[0].get('explain_url'),
                       'notes': data[0]['notes'].split('~') if data[0]['notes'] is not None else '',
                       })


def get_stats(data):
    """ Calc question stats"""

    cnt = 0
    stats_tot = 0

    stats = data.get('history', '')

    if stats is not None:
        stats_tot = len(stats.split('~')) - 1

        for i in stats.split('~'):

            if 'correct' in i:
                cnt += 1

    return stats_tot, cnt


@app.post("/quiz/grade_it")
async def grade_it(request: Request, idx: str = Form(None), chk: List = Form(None),
                   rdo: str = Form(None), viewed: bool = Form(False), submit_view: str = Form(None)):
    """ Grade the question, write to db"""

    status = ''
    correct = ''

    # | Get question, q_type from db
    data = get_questions(idx)
    q_type = data[0].get('q_type', '')
    options = data[0].get('options', '')

    if 'basic' in q_type:

        correct = [k for k, v in options.items() if v is True]

        if viewed is False:

            if rdo in correct:
                status = 'correct'
                add_history(idx, status)
                bank.add_score({str(idx): status})
            else:
                status = 'fail'
                add_history(idx, status)
                bank.add_score({str(idx): status})

    if 'multi' in q_type:

        correct = [k for k, v in options.items() if v is True]

        if viewed is False:

            if collections.Counter(correct) == collections.Counter(chk):
                status = 'correct'
                add_history(idx, status)
                bank.add_score({str(idx): status})
            else:
                status = 'fail'
                add_history(idx, status)
                bank.add_score({str(idx): status})

    if 'match' in q_type:

        # | Yucky way to get answers from FormData, del unwanted keys
        frm = await request.form()
        ans = dict(frm._list)

        ignore = ['submit_view', 'submit_nxt', 'idx', 'q_type', 'ans', 'viewed']

        for itm in ignore:
            if ans.get(itm, False) or ans.get(itm, False) == '':
                del ans[itm]

        correct = options

        if viewed is False:

            if ans == options:
                status = 'correct'
                add_history(idx, status)
                bank.add_score({str(idx): status})
            else:
                status = 'fail'
                add_history(idx, status)
                bank.add_score({str(idx): status})

    # | View button pressed
    if not submit_view:

        # | NEXT question
        nxt = bank.get_next()

        # | Next question, if not end of q list
        if nxt != 0:

            data = get_questions(nxt)

            stats_tot, stats_pass = get_stats(data[0])

            return TEMPLATES.TemplateResponse("index.html", {"request": request,
                                                             "data": data[0],
                                                             'stats_tot': stats_tot,
                                                             'stats_pass': stats_pass,
                                                             'correct': json.dumps(correct)})
        # | Final Score
        else:
            final = build_results()
            return TEMPLATES.TemplateResponse("results.html", {"request": request, "final": final})

    # | View Answer
    return TEMPLATES.TemplateResponse(
        "index.html", {"request": request,
                       "status": status,
                       "data": data[0],
                       "explain": data[0].get('explain'),
                       "explain_url": data[0].get('explain_url'),
                       'notes': data[0]['notes'].split('~') if data[0]['notes'] is not None else '',
                       'correct': json.dumps(correct),
                       'viewed': True
                       })


def get_questions(idx=''):
    """ [0=ALL or ID]"""

    cmd = f'SELECT * from tbl_questions where id = {idx}'

    if idx == 0:
        cmd = 'SELECT * from tbl_questions'

    conn = sqlite3.connect(f'{BASE_PATH}/questions.db')
    cursor = conn.execute(cmd)

    questions = []

    for row in cursor:
        itm = Question(*row).__dict__
        questions.append(itm)

    return questions


@app.post("/add_note")
async def add_note(request: Request, idx: str = Form(None), msg: str = Form(None)):
    """ Grab note in DB and append new msg """

    conn = sqlite3.connect(f'{BASE_PATH}/questions.db')

    # | Grab notes in DB
    indb = get_questions(idx)
    old_notes = indb[0].get('notes', '')

    pre = f'{datetime.datetime.now().date()}\n{msg}\n{"_" * 50}\n'
    new_notes = f'{old_notes}~{pre}'

    cmd = '''UPDATE tbl_questions SET notes = ? where id = ?'''

    cur = conn.cursor()
    cur.execute(cmd, (new_notes, idx))
    conn.commit()

    # | Reload question
    return RedirectResponse(url=f"/id/{idx}", status_code=303)


def add_history(idx: str, status: str):
    """ Add success/fail and timestamp to history """

    conn = sqlite3.connect(f'{BASE_PATH}/questions.db')

    # | Grab history in DB
    indb = get_questions(idx)
    hist = indb[0].get('history', '')
    new_hist = f'{hist}~{status}'

    cmd = '''UPDATE tbl_questions SET history = ? where id = ?'''

    cur = conn.cursor()
    cur.execute(cmd, (new_hist, idx))
    conn.commit()


@app.get('/start_quiz')
def start_quiz(request: Request):
    """ Quiz config page"""

    return TEMPLATES.TemplateResponse("start.html", {"request": request})


@app.post('/start_quiz')
async def start_quiz(request: Request, limit: str = Form(None), shuffle: bool = Form(False)):
    """ Using the config inputs, start the quiz"""

    bank.reset()

    form_data = await request.form()

    cat_lst = [itm for itm in form_data]

    # | Check if no categories were selected, then select all
    if len(cat_lst) == 2:
        cat_lst = ['concepts', 'services', 'core', 'security', 'cost']

    # | Develop query tuple, populate question bank
    cmd = f'Select * from tbl_questions where category in {tuple(cat_lst)}'

    if 'unseen' in cat_lst:
        cmd = f'Select * from tbl_questions where history is NULL'

    if 'custom' in cat_lst:
        cmd = f'Select * from tbl_questions where id > 1000'

    bank.get_db_ids(cmd, shuffle, limit)

    nxt = bank.get_next()

    data = get_questions(nxt)

    stats_tot, stats_pass = get_stats(data[0])

    return TEMPLATES.TemplateResponse("index.html", {"request": request,
                                                     "data": data[0],
                                                     'stats_tot': stats_tot,
                                                     'stats_pass': stats_pass})


def build_results():
    """ Gen stats on final quiz results"""

    correct = 0

    res = bank.get_scores()
    tot = len(res.keys())
    correct = sum('correct' in x for x in res.values())

    # | Grab category stats
    statistics = gen_category_stats(res)

    failed = tot - correct

    results = {"tot": tot, "correct": correct, "failed": failed, "data": res, "statistics": statistics}

    return results


def gen_category_stats(data):
    """Determine pass/fail by category"""

    conn = sqlite3.connect(f'{BASE_PATH}/questions.db')

    # | Build category list of seen questions
    # | -- Tuple issue if only single question
    cmd = f'Select DISTINCT(category) from tbl_questions where id in {tuple(data.keys())}'

    if len(data.keys()) == 1:
        cmd = f'Select DISTINCT(category) from tbl_questions where id = {list(data.keys())[0]}'

    print(cmd)
    cursor = conn.execute(cmd)
    categories = [cat[0] for cat in cursor]

    # | get question categories from current quiz
    cmd = f'Select id, category from tbl_questions where id in {tuple(data.keys())}'

    if len(data.keys()) == 1:
        cmd = f'Select id, category from tbl_questions where id = {list(data.keys())[0]}'
    cursor = conn.execute(cmd)

    # | Merge categories with question id and grade: 'id': {cat, grade}
    q_a_dict = {}

    for row in cursor:
        idx, val = row
        q_a_dict[str(idx)] = {'cat': val, 'grade': data.get(str(idx))}

    cat_subtotals = {}

    for category in categories:

        passing_cnt = 0
        failing_cnt = 0
        passing_q = []
        failing_q = []

        for line in q_a_dict:
            cat = q_a_dict[line].get('cat')
            grade = q_a_dict[line].get('grade')

            if cat == category:
                if grade == 'correct':
                    passing_cnt += 1
                    passing_q.append(line)
                else:
                    failing_cnt += 1
                    failing_q.append(line)

        cat_subtotals[category] = {'correct': passing_cnt, 'failed': failing_cnt,
                                   'correct_q': passing_q, 'failed_q': failing_q}

    return cat_subtotals


@app.get('/restore_db')
def restore_db(request: Request):
    """ This will restore db from questions.json"""

    memo = make_db_from_json()

    return TEMPLATES.TemplateResponse("start.html", {"request": request, 'memo': memo})


@app.get('/backup')
def restore_db(request: Request):
    """ This will backup db into JSON file: questions.json
    This includes all new questions you created"""

    memo = write_to_json_file(json_file='questions.json')

    return TEMPLATES.TemplateResponse("start.html", {"request": request, 'memo': memo})


@app.get('/editor')
def editor_home(request: Request):
    """ Edit landing page"""

    # fields = ['idx',
    #           'q_type',
    #           'q',
    #           'options1',
    #           'options2',
    #           'options3',
    #           'options4',
    #           'options5',
    #           'explain',
    #           'explain_url',
    #           'notes',
    #           'history',
    #           'misc',
    #           'category']

    # return TEMPLATES.TemplateResponse("editor.html", {"request": request, 'fields': fields})
    return TEMPLATES.TemplateResponse("editor.html", {"request": request})


@app.post('/edit')
async def edit(request: Request, form: QuestionBM = Depends(QuestionBM.as_form)):
    """ Add new questions, edit questions"""

    conn = sqlite3.connect(f'{BASE_PATH}/questions.db')

    # cmd = 'Insert into tbl_questions (id, q, options, explain, explain_url, category, q_type) ' \
    #       'VALUES (?, ?, ?, ?, ?, ?, ?)'

    cmd = 'Insert or REPLACE into tbl_questions (q, options, explain, explain_url, category, q_type) ' \
          'VALUES (?, ?, ?, ?, ?, ?)'

    opts = {form.option1: True if form.chk1 == 'True' else None,
            form.option2: True if form.chk2 == 'True' else None,
            form.option3: True if form.chk3 == 'True' else None,
            form.option4: True if form.chk4 == 'True' else None,
            form.option5: True if form.chk5 == 'True' else None,
            }

    tup = (form.q, json.dumps(opts), form.explain, form.explain_url, form.category, form.q_type)

    if form.idx:
        tup = form.idx + tup
        cmd = cmd.replace('(q', '(id, q)')
        cmd = cmd.replace('?)', '?, ?)')

    info = conn.execute(cmd, tup)

    conn.commit()

    ret_val = f'Added new item - {info.lastrowid}'

    return TEMPLATES.TemplateResponse("editor.html", {"request": request, 'memo': ret_val})


@app.get('/help')
def help_home(request: Request):
    """ Info / Donation / Help"""

    return TEMPLATES.TemplateResponse("readme.html", {"request": request})
