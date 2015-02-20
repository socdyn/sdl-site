'''
@by George Berry
@Cornell Dpt of Sociology (Social Dynamics Lab)
@Feb 2015
'''

import re
from markdown2 import markdown
from flask import Flask, url_for, render_template


#config
DEBUG = True


#make app
app = Flask(__name__)
app.config.from_object(__name__)
app.jinja_env.globals.update(enumerate=enumerate)



#processing function

def preprocess_people(md):
    '''
    splits on ~~~
    creates "cards" for each person consisting of a picture and some text
    finds picture path in ~tildes.png~
    returns [{'picture':picture, 'md':markdown},...]
    '''
    individuals = md.split('\n\n~~~\n\n')
    cards = {'grad': [], 'faculty': [], 'undergrad': []}
    for indv_md in individuals:
        try:
            picture_path = re.findall(r'~.*~', indv_md)[0]
            category = re.findall(r'&.*&', indv_md)[0]
            correct_markdown = indv_md.replace('{}\n\n'.format(picture_path), '')
            correct_markdown = correct_markdown.replace('{}\n\n'.format(category), '')
            picture_path = picture_path.strip('~')
            category = category.strip('&')
            cards[category].append({"picture": picture_path, "md": markdown(correct_markdown)})
        except Exception as e:
            print e
    return cards

def preprocess_research(md):
    '''
    splits on ~~~
    creates "cards" for each person consisting of a picture and some text
    finds picture path in ~tildes.png~
    returns [{'picture':picture, 'md':markdown},...]
    '''
    individuals = md.split('\n\n~~~\n\n')
    cards = []
    for indv_md in individuals:
        try:
            picture_path = re.findall(r'~.*~', indv_md)[0]
            correct_markdown = indv_md.replace('{}\n\n'.format(picture_path), '')
            picture_path = picture_path.strip('~')
            cards.append({"picture": picture_path, "md": markdown(correct_markdown)})
        except Exception as e:
            print e
    return cards


#routing behavior here
@app.route('/')
def draw_index():
    with open('content/greeting.md', 'rb') as f:
        greeting = markdown(f.read())
    with open('content/recent.md', 'rb') as g:
        recent = markdown(g.read())
    return render_template('mainpage.html', greeting=greeting, recent=recent)

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
