from flask import Flask, render_template, request, url_for, flash, redirect
from vectorPrediction import *
from time import sleep
import os, shutil



from threading import Thread
app = Flask(__name__,static_folder='images',)
app.config["CACHE_TYPE"] = "null"
app.config['SECRET_KEY'] = 'b1808f24613321f9007f0e8b31759bc269e8fc6a6a2fb51d'


folder = './images/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))





messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/', methods=('GET', 'POST'))
def index():
    my_message='null';
    print('here')
    if request.method == 'POST':
        color1   = request.form['color1']
        color2   = request.form['color2']
        color3   = request.form['color3']
        color4   = request.form['color4']
        color5   = request.form['color5']
        color6   = request.form['color6']
        color7   = request.form['color7']
        color8   = request.form['color8']
        color9   = request.form['color9']



        prediction_value = perform_task(color1,color2,color3,color4,color5,color6,color7,color8,color9)
        if prediction_value[0] == 0:
          my_message= "Not Critical"
          print("Not Critical")
        elif prediction_value[0] == 1:
          my_message= "Critical"
          print("Critical Color")
        else:
          print("Weird Result")

        


        

    return render_template('criticalcolor.html', messages=my_message)





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
