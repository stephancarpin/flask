

from flask import Flask, render_template, request, url_for, flash, redirect
from vectorPrediction import *
from lrlime import *
from time import sleep
import os, shutil
from threading import Thread
import pandas as pd
import math




# plt.switch_backend('Agg')
# print("Using:",matplotlib.get_backend())


app = Flask(__name__,static_folder='assets')
app.config["CACHE_TYPE"] = "null"
app.config['TESTING']    = True
app.testing = True
app.config['SECRET_KEY'] = 'b1808f24613321f9007f0e8b31759bc269e8fc6a6a2fb51d'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


folder = './assets/images/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

initializtion()




csv_data= pd.read_csv('./data/CriticalColours.csv',header=0)

headers = csv_data.columns[0:19]



print(headers)



@app.route('/', methods=('GET', 'POST') )
def index():
    my_message="null"
    array_inputs=[]
    if request.method == 'POST':

        for index, h in enumerate(headers):
            print(index,h)
            if len(request.form[h]):
                array_inputs.append(request.form[h])
            else:
                array_inputs.append(0)
                
        # prediction_value = perform_task_LR(array_inputs,csv_data)[0]
        prediction_value = perform_task_LR(array_inputs,csv_data)[0]

        if prediction_value[0] == 0:
          my_message  = "Not Critical"
          print("Not Critical")
        elif prediction_value[0] == 1:
          my_message  = "Critical"
          print("Critical Color")
        else:
          print("Weird Result")

    return render_template('index.html', messages=my_message,html_headers= headers)
