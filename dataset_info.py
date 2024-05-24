import numpy as numpy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
heart_data=pd.read_csv(r'C:\Users\syeme\Downloads\heart.csv')
print("The intial data in data set:",heart_data)
print("The number of rows and columns of the data set respectively:",heart_data.info)
print("Statistical measures about the data:",heart_data.describe())
#Target:1-->Defective Heart
#Target:0-->Healthy Heart
print("Number of healthy hearts in the given data set:",heart_data['target'].value_counts())