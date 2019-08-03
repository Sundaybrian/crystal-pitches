from flask import render_template,request,redirect,url_for,abort
from . import main


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    pitches=[
        {
            'author':"Sunday Brian0",
            'title':'MatchdayExperience',
            'content':'Lorem Lorem',
            'date_posted':'July 13,2019'
        },
          {
            'author':"Sunday Brian1",
            'title':'MatchdayExperience',
            'content':'Lorem Lorem',
            'date_posted':'July 13,2019'
        },
          {
            'author':"Sunday Brian2",
            'title':'MatchdayExperience',
            'content':'Lorem Lorem',
            'date_posted':'July 13,2019'
        },
          {
            'author':"Sunday Brian3",
            'title':'MatchdayExperience',
            'content':'Lorem Lorem',
            'date_posted':'July 13,2019'
        }
    ]
    return render_template('index.html',title='home',pitches=pitches)