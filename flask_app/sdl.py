'''
@by George Berry
@Cornell Dpt of Sociology (Social Dynamics Lab)
@Feb 2015
'''
import sqlite3
from markdown2 import markdown
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

#config
#DATABASE = 'sdl.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#start app
app = Flask(__name__)
app.config.from_object(__name__)
#app.jinja_env.globals.update(markdown=markdown)

#returns first n projects for sidebar display
def get_first_projects(text, n):
    pass

@app.route('/')
def draw_index():
    with open('content/greeting.md', 'rb') as f:
        greeting = markdown(f.read())
    #with open('recent.md', 'rb') as g:
    #    recent = get_first_research(f.read(), n)
    return render_template('mainpage.html', greeting=greeting) #, recent=recent)


@app.route('/people')
def draw_people():
    with open('content/people.md', 'rb') as f:
        people = markdown(f.read())
    return render_template('people.html', people=people)

@app.route('/research')
def draw_research():
    with open('content/research.md', 'rb') as f:
        research = markdown(f.read())
    return render_template('research.html', research=research)

@app.route('/contact')
def draw_contact():
    with open('content/contact.md', 'rb') as f:
        contact = markdown(f.read())
    return render_template('contact.html', contact=contact)


#run app
if __name__ == '__main__':
    app.run()
