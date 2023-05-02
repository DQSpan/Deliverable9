# -*- coding: utf-8 -*-
"""Deliverable9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/186mtH_OCKXXAYVqKQdgyMQ9kaaVDNJYu

STEP 1: We'll use a model using the Boston Housing dataset to forecast the median price of a property based on a dataset attribute.

STEP 2:
"""

import pandas as pd
df = pd.read_csv('/content/boston_housing.csv')
df.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

features_names = df.columns.to_list()[:-1]
X = df[features_names] 
Y = df['MEDV']

"""STEP 3:"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

myLR = LinearRegression()
myLR.fit(X_train, Y_train) 

pred = myLR.predict(X_test)

pred

def MAPE(Y, pred): # MAPE: Mean Abs Percentage Error
  l1 = list(Y)
  l2 = list(pred)
  er = []
  for i in range(len(l1)):
    e = np.abs(l1[i]-l2[i])
    er.append(e/l1[i])
  return np.mean(er)

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, pred)))
print('MAPE:', MAPE(Y_test, pred)*100, "%")

"""Mean Absolute Error: 3.668330148135719
Mean Squared Error: 29.782245092302375
Root Mean Squared Error: 5.457311159564055
MAPE: 17.54993780061571 %



"""

import matplotlib.pyplot as plot
plot.figure(figsize = (6, 4))
plot.scatter(x = Y_test, y = pred, color = 'Tab:red')
plot.xlabel('Actual House Price', fontsize = 15)
plot.ylabel('Prediction', fontsize = 15)
plot.show()

print('The model r2 score is: {}'.format(my_linear_regression.score(X_train, Y_train)))

"""The model r2 score is: 0.7697699488741149

STEP 4: Based on the given test data, we have developed predictions, as shown by the linear regression model. Therefore, based on the actual housing price data that we have, we can use the model to predict housing prices. The model works pretty well based on the metrics supplied (MAE, MSE and Root MSE, MAPE). According to our MAPE, the inaccuracy is about 17.5%. According to the scatterplot's R2, the independent variable's variation may account for 77% of the variance in the dependent variable. By gathering more information or identifying and deleting outliers, we can increase this figure.
"""