from markdown2 import markdown
import re

with open('content/people.md', 'rb') as f:
    people = f.read()

def preprocess_markdown(md):
    individuals = md.split('\n\n~~~\n\n')
    cards = []

    for i in individuals:
        picture_path = re.findall(r'~.*~', i)[0]
        correct_markdown = i.replace('{}\n\n'.format(picture_path), '')
        picture_path = picture_path.strip('~')
        cards.append([picture_path, markdown(correct_markdown)])

    return cards

print preprocess_markdown(people)