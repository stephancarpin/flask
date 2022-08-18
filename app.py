from flask import Flask, render_template, request, url_for, flash, redirect
from machine_learning import *
from time import sleep




from threading import Thread
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b1808f24613321f9007f0e8b31759bc269e8fc6a6a2fb51d'







messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)




@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title   = request.form['title']
        content = request.form['content']




        perform_task()


        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
