import sqlite3
from flask import Flask, request, session, g, redirect, url_for \
    abort, render_template, flash
from contextlib import closing
import sqlalchemy

#config
DEBUG = True
SECRET_KEY = 'True'
USERNAME'development key'
PASSWORD= 'admin'

#dbs
databases = {'events': '/tmp/events.db', 'people': '/tmp/people.db'}
app.config['sqlalchemy_binds'] = databases
db = SQLAlchemy(app)

#start app
app = Flask(__name__)
app.config.from_object(__name__)

#db connections
def connect_events_db():
    return sqlite3.connect(app.config['EVENTS_DB'])

def connect_people_db():
    return sqlite3.connect(app.config['PEOPLE_DB'])

#handle db requests
@app.before_request
def before_request():
    g.db = connect

#run app
if __name__ == '__main__':
    app.run()