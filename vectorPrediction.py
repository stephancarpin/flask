import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
import matplotlib
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
# For data manipulation
import pandas as pd
# To plot
import matplotlib.pyplot as plt
import seaborn

plt.switch_backend('Agg')
print("Using:",matplotlib.get_backend())

def perform_task(color1,color2,color3,color4,color5,color6,color7,color8,color9):
	# Machine learning classification
	
    

	# Step 2: Fetch data


	data= pd.read_csv('./data/critical_colours_grouped.csv',header=0)

	data= data.dropna()

	y = np.array(data['Class']);

	x = data.loc[:, data.columns != 'Class']
	y = np.array(data['Class']);
	X = np.array(x);
	split_percentage = 0.7
	split = int(split_percentage*len(data))
	# Train data set
	X_train = X[:split]
	y_train = y[:split]
	# Test data set
	X_test = X[split:]
	y_test = y[split:]
	cls = SVC().fit(X_train, y_train)
	accuracy_train = accuracy_score(y_train, cls.predict(X_train))
	accuracy_test  = accuracy_score(y_test, cls.predict(X_test))
	print('\nTrain Accuracy:{: .2f}%'.format(accuracy_train*100))
	print('Test Accuracy:{: .2f}%'.format(accuracy_test*100))


	cls.score(X, y)
	confusion_matrix(y, cls.predict(X))

	cm = confusion_matrix(y, cls.predict(X))
	fig, ax = plt.subplots(figsize=(8, 8))
	ax.imshow(cm)
	ax.grid(False)
	ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
	ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
	ax.set_ylim(1.5, -0.5)
	for i in range(2):
	    for j in range(2):
	        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
	plt.savefig("./images/confusion_matrix.jpg")
	print(classification_report(y, cls.predict(X)))


	X_input_test   = np.array([color1,color2,color3,color4,color5,color6,color7,color8,color9])
	arr_2d         = np.reshape(X_input_test,[1,9])
	# print(arr_2d)
	prediction= cls.predict(arr_2d)
	print(prediction)
	return [prediction,x]
	













