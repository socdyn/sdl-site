import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

#config
DATABASE = '/tmp/sdl.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD= 'default'

#start app
app = Flask(__name__)
app.config.from_object(__name__)

#db connections
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#setup database from within python
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


#handle db requests
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


#pages here---

#main page: needs a stream of recent research and recent events
@app.route('/')
def draw_index():
    #sets up a cursor to query the DB
    cur = g.db.execute('select headline, content from events by time desc')
    #makes a dictionary of headline: content
    events = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #renders that shit, passing the events events
    return render_template('mainpage.html', events=events)


#run app
if __name__ == '__main__':
    app.run()