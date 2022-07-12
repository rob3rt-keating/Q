import os
import json
import sqlite3
from pathlib import Path
from helpers import Question

BASE_PATH = Path(__file__).resolve().parent


def create_table(filename=''):

    conn = sqlite3.connect(f'{BASE_PATH}/{filename}')

    cmd = """CREATE TABLE tbl_questions
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    q TEXT NOT NULL,
    options JSON NOT NULL,
    explain TEXT,
    explain_url TEXT,
    notes TEXT,
    history TEXT,
    category TEXT,
    q_type TEXT,
    misc TEXT,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);"""

    cmd_index = """ CREATE UNIQUE INDEX idx_app_id on tbl_questions(id);"""

    cmd_autoinc = """UPDATE sqlite_sequence SET seq = 1000 WHERE NAME = 'tbl_questions';"""

    conn.execute(cmd)
    conn.execute(cmd_index)
    conn.execute(cmd_autoinc)
    conn.close()


def write_to_json_file(json_file=''):
    """ Get questions, write to new json file"""

    # | Delete questions.json file
    if os.path.exists(f'{BASE_PATH}/questions.json'):
        os.remove(f'{BASE_PATH}/questions.json')

    data = get_questions(idx='0')

    with open(f'{BASE_PATH}/questions.json', 'w') as write_file:
        json.dump(data, write_file, indent=4)

    return f"Backed up questions to {BASE_PATH}/questions.json"


def read_db(idx='', tmp_db=''):
    """ [ALL= 0 or ID]"""

    cmd = f'SELECT * from tbl_questions where id = {idx}'

    if idx == '0':
        cmd = 'SELECT * from tbl_questions'

    conn = sqlite3.connect(f'{BASE_PATH}/{tmp_db}')
    cursor = conn.execute(cmd)

    questions = []

    for row in cursor:
        idx, q, options, explain, explain_url, notes, history, category, q_type, misc, timestamp = row

        itm = {
            'id': idx,
            'q': q,
            'options': json.loads(options),
            'explain': json.loads(explain),
            'explain_url': json.loads(explain_url),
            'notes': notes,
            'history': history,
            'category': category,
            'q_type': q_type,
            'misc': misc,
            'timestamp': timestamp
        }
        questions.append(itm)

    return questions


def get_questions(idx=''):
    """ [0=ALL or ID]"""

    cmd = f'SELECT * from tbl_questions where id = {idx}'

    if idx == '0':
        cmd = 'SELECT * from tbl_questions'

    conn = sqlite3.connect(f'{BASE_PATH}/questions.db')
    cursor = conn.execute(cmd)

    questions = []

    for row in cursor:
        itm = Question(*row).__dict__
        questions.append(itm)

    return questions


def add_to_sql(items, filename=''):

    conn = sqlite3.connect(f'{BASE_PATH}/{filename}')

    for itm in items:

        print(itm["id"])

        cmd = 'Insert into tbl_questions (id, q, options, explain, explain_url, category, q_type) ' \
              'VALUES (?, ?, ?, ?, ?, ?, ?)'

        conn.execute(cmd, (int(itm["id"]), itm["q"], json.dumps(itm["options"]),
                           itm.get("explain"), itm["explain_url"],
                           itm.get("category", ""), itm["q_type"]))
        conn.commit()

    print('Completed new database build/restore')


def make_db_from_json(filename='questions.db', json_file='questions.json'):
    """ Delete old DB file, Read new json formatted file into mem, write into sqlite3 db"""

    # | Delete questions.db
    if os.path.exists(f'{BASE_PATH}/questions.db'):
        os.remove(f'{BASE_PATH}/questions.db')

    create_table(filename)

    f = open(f'{BASE_PATH}/{json_file}')
    data = json.load(f)

    add_to_sql(data, filename=filename)

    return 'Completed new database build/restore'
