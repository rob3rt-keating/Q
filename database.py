import os
import json
import sqlite3
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent


def create_table(filename=''):

    conn = sqlite3.connect(f'{BASE_PATH}/{filename}')


    cmd = """CREATE TABLE tbl_questions
    (id INT PRIMARY KEY,
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

    conn.execute(cmd)
    conn.close()


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
