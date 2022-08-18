import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
import matplotlib
import matplotlib.pyplot as plt

plt.switch_backend('Agg')
print("Using:",matplotlib.get_backend())




def perform_task():
    data = pd.read_csv("./data/dataset.csv")
    data.shape
    df = pd.DataFrame(data)
    print(df)
    x = df.iloc[:,:-2]
    print(x)
    y = df.iloc[: , -2:]
    print(y)
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [4])], remainder= 'passthrough')
    x = np.array(ct.fit_transform(x))

    print(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2,random_state= 1)
    sc_x=StandardScaler()
    x_train=sc_x.fit_transform(x_train)
    x_test=sc_x.transform(x_test)
    x_train

    plt.scatter(data.iloc[:,0],data.iloc[:,2])
    plt.xlabel('Count')
    plt.ylabel('Density')
    plt.title('Scatter plot')

    # Saving the figure.
    plt.savefig("./images/output3.jpg")

    # Saving figure by changing parameter values
    plt.savefig("./images/output2", facecolor='y', bbox_inches="tight",
                                    pad_inches=0.3, transparent=True)



    # Creating data
    year = ['2010', '2002', '2004', '2006', '2008']
    production = [25, 15, 35, 30, 10]

    # Plotting barchart
    plt.bar(year, production)

    # Saving the figure.
    plt.savefig("./images/output.jpg")

    # Saving figure by changing parameter values
    plt.savefig("./images/output1", facecolor='y', bbox_inches="tight",
                                pad_inches=0.3, transparent=True)


















