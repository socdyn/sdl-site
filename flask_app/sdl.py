'''
@by George Berry
@Cornell Dpt of Sociology (Social Dynamics Lab)
@October 2013
'''
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

#config
DATABASE = 'sdl.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

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
    cur = g.db.execute('select headline, description from research')
    #makes a dictionary of headline: content
    research = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]

    #sets up a cursor to query the DB
    cur = g.db.execute('select headline, description from events')
    #makes a dictionary of headline: content
    events = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]

    return render_template('mainpage.html', research=research, events=events)


@app.route('/research')
def draw_research():
    #sets up a cursor to query the DB
    cur = g.db.execute('select headline, description from research')
    #makes a dictionary of headline: content
    research = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('research.html', research=research)


@app.route('/people')
def draw_people():
    #sets up a cursor to query the DB
    cur = g.db.execute('select headline, description from people')
    #makes a dictionary of headline: content
    people = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('people.html', people=people)


@app.route('/events')
def draw_events():
    #sets up a cursor to query the DB
    cur = g.db.execute('select headline, description from events')
    #makes a dictionary of headline: content
    events = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('events.html', events=events)


@app.route('/resources')
def draw_resources():
    #sets up a cursor to query the DB
    cur = g.db.execute('select headline, description from resources')
    #makes a dictionary of headline: content
    resources = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('resources.html', resources=resources)


#@app.route('/edit')
    

#@app.route('/login')


#run app
if __name__ == '__main__':
    app.run()
