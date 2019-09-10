"""
This module mirrors module_run, but uses a subset of the training db
as the test data to check the accuracy of the model.py module.
It first calculates the parameters for the logistic regression prediciton,
then uses them to predict the level of each word, and compares it to the original level.
An accuracy percent line is documented out in the model.py module, but is userful
when running this module.
Note: throughout, arrays are used as they are exponentionally more efficient
for calculations, especially as datasets get larger.
In flow, the model.py comes next.

Input: training and test datasets.
Output: formatted X_train, Y_train, X_test, Y_test passed through model.py
@author: yaman
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import csv
import sqlite3
from LearnToGo.logistic_regression import model #import logistic regression model

X_train_list= []
Y_train_list = []
X_test_list = []
Y_test_list = []

con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
cur = con.cursor()
for row in cur.execute("SELECT word_length, word_syllables, word_usage_rank, word_level from langdata_training_logistic"):
        row = [float(i) for i in row]
        X_train_list.append(row[0:3])
        Y_train_list.append(row[3])
X_train=np.array(X_train_list).T
X_train=X_train.astype(float)
Y_train=np.array(Y_train_list)

Y_train=np.reshape(Y_train,(len(Y_train),1)).T
print("This is where it's at",Y_train)

con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
cur = con.cursor()

with open('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/logistic_regression/langdata_test_logistic.csv', 'r') as test_file:
    test_data = csv.reader(test_file, delimiter=',')
    for row in test_data:
        X_test_list.append(row[0:3])
        Y_test_list.append(row[3])

X_test=np.array(X_test_list).T
Y_test=np.array(Y_test_list)
Y_test=np.reshape(Y_test,(len(Y_test),1)).T

model.model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False)
