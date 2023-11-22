# -*- coding: utf-8 -*-
"""Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yUO9psxYeb5fESfWmuM6NcjZr-pVykyQ

# **Implementing Linear Regression classifier**

## Introduction

Regression analysis is used to understand which among the independent variables are related
to the dependent variable, and to explore the forms of these relationships. Besides, regression
analysis is widely used for prediction, forecasting, and classification where its use has considerable
connect with the field of machine learning. In this assignment I will implement the Linear
Regression classifier using the python library, the numerical method technique and lastly the
polyfit built in function.

## Objectives

*   To understanding the cost function for Linear regression
*   To knowing how to find the coefficients for Linear Regression
*   To plotting the results obtained through numerical, library and polyfit operations in python

## Library Imports
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

"""# **Task 01:**



**Loading the dataset**
"""

from google.colab import drive
drive.mount('/content/drive')

path = "/content/drive/MyDrive/Real_estate - Real_estate.csv"
df = pd.read_csv(path)            # Dataset is now stored in a Pandas Datafrase
df.head()                         # head() will show the first 5 rows of dataset

"""**Correlate it to find two most strongly correlated features.**"""

plt.figure(figsize=(8,5))
cor = df.corr()                 #corr() is used to find the pairwise correlation of all columns in the dataset
sns.heatmap(cor, annot=True)
plt.show()

"""Here two most strongly positive correlated features are ***No of stores*** and ***House Price***

# **Task 02:**
**Extracting the two features from the previous**
"""

df = df.drop(['Trans date', 'House age', 'Distance station', 'Latitude', 'Longitude'], axis=1)
df.head()

"""**Plotting those two features using scatterplot.**"""

plt.figure(figsize=(8,5))
plt.scatter(df['No of stores'], df['House Price'], c ="blue", marker ="o", alpha = 0.5)
plt.xlabel('No. of Stores(X)')
plt.ylabel('House Price(Y)')
plt.title('Scatter Plot')
plt.grid(True)
plt.show()

"""Here ***No of store*** is independent variable and ***House Price*** is dependent variable.

# **Task 03:**
**Using those two features to split the dataset into training and testing sets.**

The main idea of splitting the dataset into a validation set is to prevent our model from overfitting.
"""

x = np.array(df['No of stores']).reshape(-1,1)
y = np.array(df['House Price']).reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

"""Here I have divided the dataset into 80%-20%. Where 80% training set and 20% testing set.

**Implementing the
Linear Regression classifier from the python library.**
"""

reg = LinearRegression()
reg.fit(x_train, y_train)

"""**Displaying the coefficient,
intercept(b_1, b_0) and the test accuracy for this model.**
"""

b_1 = reg.coef_
print('The coefficient is', b_1)

b_0 = reg.intercept_
print('The y-intercept is', b_0)

test_acc = reg.score(x_test,y_test)
print('Test Accuracy for this model is', test_acc)

"""# **Task 04:**
**Displaying the mean absolute error (MAE), mean squared error (MSE) and R2-score for this
model using built in function.**
"""

y_pred = reg.predict(x_test)                       # The predicted value of y

MAE =  mean_absolute_error(y_test, y_pred)         #The mean absolute error measures the average differences between predicted values and actual values.
print('The mean absolute error (MAE) is', MAE)

MSE =  mean_squared_error(y_test, y_pred)     #The MSE is just like MAE, but squares the difference before summing them all instead of using the absolute value.
print('The mean squared error (MSE) is', MSE)

R2_score =  r2_score(y_test, y_pred)
print('The R2-score is', R2_score)

"""# **Task 05:**
**Plotting the actual test data(xtest,ytest) in the form of a scatter plot and the fitted line for the
predicted data(xtest,ypred) over it for this model.**
"""

plt.scatter(x_test , y_test)
plt.plot(x_test , y_pred, c ="red")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression\n b1 = 2.65, b0 = 27.33')
plt.grid(True)
plt.show ()

"""**Displaying the residuals(line from the
actual data onto the predicted line) and its distance.**
"""

# Calculating the residuals
Residuals = y_test - y_pred                                             #residuals = actual y(yi) − predicted y (^yi)

# Calculating the distance
pointA = (x_test, y_test)
pointB = (x_test, y_pred)

def calc_distance(p1, p2):
  return np.sqrt(pow((p1[0] - p2[0]),2) + pow((p1[1] - p2[1]),2))       #Euclidean Distance = √[(x2 – x1)^2 + (y2 – y1)^2]

distance = calc_distance(pointA, pointB)

# Displaying the residuals and distances
print("""Residuals \t \tDistance""")
for x, y in zip(Residuals, distance):
    print(x, y, sep='\t\t')

# Plotting the residuals (line from the actual data onto the predicted line)
plt.scatter(x_test , y_test, c = 'red', marker ="x")
for i in range(len(x_test)):
        lineXdata = (x_test[i], x_test[i])
        lineYdata = (y_test[i], y_pred[i])
        plt.plot(lineXdata, lineYdata, c ="green")
plt.plot(x_test , y_pred, c = 'blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Residuals\n (line from the actual data onto the predicted line)')
plt.grid(True)

"""# **Task 06:**

**Implementing the Linear Regression model on the dataset using numerical methods and displaying its coefficient and intercept(b_1, b_0).**
"""

x = np.array(df['No of stores']).reshape(-1,1)
y = np.array(df['House Price']).reshape(-1,1)

# number of observations/points
n = np.size(x)

# mean of x and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# calculating cross-deviation and squared-deviation about x
Sxy = np.sum(x*y) - n*x_mean*y_mean           # Sxy is the sum of cross-deviations of y and x
Sxx = np.sum(x*x) - n*pow(x_mean,2)           # Sxx is the sum of squared-deviations of x

# calculating regression coefficients and intercept
b1 = Sxy/Sxx
b0 = y_mean - b1 * x_mean

# Displaying the coefficient and intercept
print('Coefficient is', b1)
print('Intercept is', b0)

"""**Displaying the best fitted line over the actual data.**"""

Y_pred = b1 * x + b0                   # The equation of regression line

plt.figure(figsize=(8,5))
plt.scatter(x, y)
plt.plot(x, Y_pred, color = 'red')
plt.grid(True)
plt.title('Numerical Methods\n b1 = 2.64, b0 = 27.18')
plt.xlabel('X')
plt.ylabel('Y')

"""# **Task 07:**
**Displaying the mean absolute error (MAE), mean squared error (MSE) and R2-score for the
numerical method approach without using any built in function.**
"""

y_residue = y - Y_pred
y_tot = y - y_mean
sy = np.sum(pow(y_residue,2))
ss = np.sum(pow(y_tot,2))

mae = (np.sum(abs(y_residue)))/n
print('Mean Absolute Error(MAE) is', mae)

mse = sy/n
print('Mean Squared Error(MSE) is', mse)

R2 = 1- (sy/ss)
print('R2-score is', R2)

"""# **Task 08:**
**Implementing the Linear Regression model on the dataset using the polyfit function and
displaying its coefficient and intercept(b_1, b_0).**
"""

x1 = np.array(df['No of stores'])
y1 = np.array(df['House Price'])
p = np.polyfit(x1,y1,1)                      #The np.polyfit() function, accepts three different input values: x, y and the polynomial degree.
yp_pred = np.polyval(p,x1)

b1 = p[0]
b0 = p[1]
print('Coefficient is', b1)
print('Intercept is', b0)

"""**Displaying the best fitted line over the actual
data.**
"""

plt.figure(figsize=(8,5))
plt.scatter(x1, y1)
plt.plot(x1, yp_pred, color = 'red')
plt.grid(True)
plt.title('Polyfit\n b1 = 2.64, b0 = 27.18')
plt.xlabel('X')
plt.ylabel('Y')

"""# **Task 09:**
**Comparing the best fitted line for the above mentioned methods.**
"""

fig, axs = plt.subplots(1,3, figsize=(20,5))

axs[0].scatter(x, y, marker ="x")
axs[0].plot(x, Y_pred, c = 'red')
axs[0].set(xlabel = 'X')
axs[0].set(ylabel = 'Y')
axs[0].set_title('Numerical', c = 'red')
axs[0].grid(True)

axs[1].scatter(x_test , y_test, marker ="x")
axs[1].plot(x_test , y_pred, c ='green')
axs[1].set(xlabel = 'X')
axs[1].set(ylabel = 'Y')
axs[1].set_title('Linear Regression', c ='green')
axs[1].grid(True)

axs[2].scatter(x1, y1, marker ="x")
axs[2].plot(x1, yp_pred, c = 'orange')
axs[2].set(xlabel = 'X')
axs[2].set(ylabel = 'Y')
axs[2].set_title('Polyfit', c = 'orange')
axs[2].grid(True)

plt.show()

"""## Conclusion:
Linear regression is the most used statistical modeling technique in Machine Learning today. It forms a vital part of Machine Learning, which involves understanding linear relationships and behavior between two variables, one being the dependent variable while the other one being the independent variable. By completing this assignment, I have learned how to implement linear regression classifier. At first, I import all the libraries which I need to execute this program and then I have load the dataset in google colab (Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning), correlate it and find strongly correlated features, also plot them using scatter plot. Also I split the dataset into training and testing sets. I also implement the linear regression. Then display the coefficients, intercept (b1, b0), test accuracy, mean absolute error (MAE), mean squared error (MSE) and R2 score using built-in function and numerical method both.
Also I have plot the actual test data(xtest, ytest) in the form of a scatter plot and the fitted line for the predicted data(xtest, ypred) over it and display residuals and distance of it. I have also display the best fitted line over the actual data after implementing the Linear Regression model on the dataset using numerical methods. Then implement the Linear Regression model on the dataset using the polyfit function and display its coefficient and intercept (b1, b0) and the best fitted line over the actual data as well. At last, I have compared the best fitted line for the numerical, linear regression and ployfit methods using subplot.



"""