from markdown2 import markdown
import re, datetime

#processing function

def preprocess_people(md):
    '''
    splits on ~~~
    creates "cards" for each person consisting of a picture and some text
    finds picture path in ~tildes.png~
    returns [{'picture':picture, 'md':markdown},...]
    '''
    individuals = md.split('\n\n~~~\n\n')
    cards = {'current':[], 'former': []}
    for indv_md in individuals:
        picture_path = re.findall(r'~.*~', indv_md)[0]
        category = re.findall(r'&.*&', indv_md)[0]

        #remove picture path and category
        correct_markdown = indv_md.replace('{}\n\n'.format(picture_path), '')
        correct_markdown = correct_markdown.replace('{}\n\n'.format(category), '')

        #format picture path and category
        picture_path = picture_path.strip('~')
        category = category.strip('&')

        cards[category].append({"picture": picture_path, "md": markdown(correct_markdown)})


    #sort by last name

    return cards

def preprocess_research(md):
    '''
    splits on ~~~
    creates "cards" for each person consisting of a picture and some text
    finds picture path in ~tildes.png~
    returns [{'picture':picture, 'md':markdown},...]
    '''
    projects = md.split('\n\n~~~\n\n')
    cards = []
    for project in projects:
        try:
            #get picture path
            picture_path = re.findall(r'~.*~', project)[0]

            #remove picture path
            correct_markdown = project.replace('{}\n\n'.format(picture_path), '')

            picture_path = picture_path.strip('~') #format

            cards.append({"picture": picture_path, "md": markdown(correct_markdown)})
        except Exception as e:
            raise e
    return cards


def preprocess_recents(md):
    events = md.split('\n\n~~~\n\n')
    cards = []

    for event in events:
        event_dict = {}

        date = re.findall(r'&.*&', event)[0]
        date = parse_date(date.strip('&')) #date class
        datestr = str(date) #date str
        event_dict['date'] = date


        correct_markdown = re.sub(r'&.*&', datestr, event)

        print(correct_markdown)
        event_dict['md'] = markdown(correct_markdown)
        print(event_dict['md'])

        cards.append(event_dict)

    #only return first three (most recent)
    cards = sorted(cards, key=lambda x:x['date'], reverse=True)[:3]
    cards.reverse()

    return [x['md'] for x in cards] 


def parse_date(full_datestring):
    '''
    dates are in format:
        2015.04
        2015.04.27
        2015.04.27-2015.04.28
        2015.04-2015.05

    i.e. we can have a range, and we can have YYYY.MM.DD or just YYYY.MM

    if range, split, and then apply a parsing function to both sides

    only returns first one for now
    '''
    if '-' in full_datestring:
        d1, d2 = full_datestring.split('-')
        d1, d2 = make_date(d1), make_date(d2)
        return d1
    else:
        d1 = make_date(full_datestring)
        return d1


def make_date(datestring):
    '''
    assign middle of month for no explicit day
    '''
    datelist = datestring.split('.')

    if len(datelist) == 2:
        datelist = [datelist[0], datelist[1], '15']

    datelist = [int(x) for x in datelist]
    return datetime.date(*datelist)