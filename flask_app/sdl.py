'''
@by George Berry
@Cornell Dpt of Sociology (Social Dynamics Lab)
@Feb 2015
'''

from flask import Flask, url_for, render_template
from random import shuffle
from markdown2 import markdown
from md_parser import preprocess_people, preprocess_research, preprocess_recents



#config
DEBUG = True

#make app
app = Flask(__name__)
app.config.from_object(__name__)

#routing behavior here
@app.route('/')
def draw_index():
    with open('content/greeting.md', 'rb') as f:
        greeting = markdown(f.read())
    with open('content/recent.md', 'rb') as g:
        recents = preprocess_recents(g.read())
    return render_template('mainpage.html', greeting=greeting, recents=recents)

@app.route('/people')
def draw_people():
    with open('content/people.md', 'rb') as f:
        people = preprocess_people(f.read())
    return render_template('people.html', people=people)

@app.route('/research')
def draw_research():
    with open('content/research.md', 'rb') as f:
        research = preprocess_research(f.read())
    return render_template('research.html', research=research)

@app.route('/contact')
def draw_contact():
    with open('content/contact.md', 'rb') as f:
        contact = markdown(f.read())
    return render_template('contact.html', contact=contact)


#run app
if __name__ == '__main__':
    app.run()
