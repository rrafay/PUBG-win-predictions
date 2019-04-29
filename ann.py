# -*- coding: utf-8 -*-
"""ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17V2eipupitAbg1C5gGTwQj7Re_KSN7Em
"""

print("HI")

print("THis is ML ")

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

dataset = pd.read_csv('train_V2.csv')

X = dataset.iloc[:, [3,5,7,8,9,11,14,16,17,18,25,26,27]].values
y = dataset.iloc[:, 28].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
scaled = StandardScaler()
X_train = scaled.fit_transform(X_train)
X_test = scaled.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

regressor = Sequential()

# Adding the input layer and the first hidden layer
regressor.add(Dense(units = 7, kernel_initializer = 'uniform', activation = 'relu', input_dim = 13))

# Adding the second hidden layer
regressor.add(Dense(units = 7, kernel_initializer = 'uniform', activation = 'relu'))



# Adding the output layer
regressor.add(Dense(units = 1,  kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
regressor.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
regressor.fit(X_train, y_train, batch_size = 13, epochs = 70)



# Predicting the Test set results
y_pred = regressor.predict(X_test)



score, acc = regressor.evaluate(X_test, y_test, batch_size=13)
print('Test loss score:', score)
print('Test accuracy:', acc)

"""**Score** is the evaluation of the loss function for a given input.

Training a network is finding parameters that minimize a loss function (or cost function).

The cost function here is the binary_crossentropy.

For a target T and a network output O, the binary crossentropy can defined as

f(T,O) = -(T*log(O) + (1-T)*log(1-O) )

So the **score** you see is the evaluation of that.

If you feed it a batch of inputs it will most likely return the mean loss.

If your model has lower loss (at test time), it should often have lower prediction error.
"""





"""**Logistic Regression on the same dataset**"""

X = dataset.iloc[:, [3,5,7,8,9,11,14,16,17,18,25,26,27]].values
y = dataset.iloc[:, 28].values
y = y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
scaled = StandardScaler()
X_train = scaled.fit_transform(X_train)
X_test = scaled.transform(X_test)

#Logistic Regression
from sklearn.linear_model import LogisticRegression

logistic_regression = LogisticRegression()
logistic_regression.fit(X_train,y_train)
predictions = logistic_regression.predict(X_test)

score = logistic_regression.score(X_test,y_test)
print("Logistic regression score is:" , score)

test = pd.read_csv('test_V2.csv')

#Make a Predictions Column
test = test.assign(Preds = "")

#Make Predcitions on test set
test_x = test.iloc[:, [3,5,7,8,9,11,14,16,17,18,25,26,27]].values
test_y = test.iloc[:, 28].values

test_predictions = logistic_regression.predict(test_x)

#Transfer predictions to CSV
submission =  pd.read_csv('sample_submission_V2.csv')
submission['winPlacePerc'] = test_predictions

#Make CSV
submission.to_csv('submission_file.csv', index=False)

submission_file = pd.read_csv("submission_file.csv")



