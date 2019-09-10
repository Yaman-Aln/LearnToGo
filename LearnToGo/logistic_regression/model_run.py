#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module calculates the parameters for the logistic regression prediction,
then uses them to predict the level of each word in the words table.
testdata_accuracy mirrors this with a pre-known test dataset and provides accuracy.

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
from LearnToGo.logistic_regression import model

X_train_list= []
Y_train_list = []
X_test_list = []
Y_test_list = []

con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
cur = con.cursor()
for row in cur.execute("SELECT word_length, word_syllables, word_usage_rank, word_level from langdata_training_logistic"):
    try:
        row = [float(i) for i in row]
        X_train_list.append(row[0:3])
        Y_train_list.append(row[3])
    except:
        row = row

X_train=np.array(X_train_list).T
X_train=X_train.astype(float)
Y_train=np.array(Y_train_list)
Y_train=np.reshape(Y_train,(len(Y_train),1)).T

cur.close()
con.close()

con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
cur = con.cursor()

for row in cur.execute("SELECT word_length, word_syllables, word_usage_rank from words"):
        try:
            row = [int(i) for i in row]
        except ValueError:
            row = [8,3,15000]
        X_test_list.append(row[0:3])

X_test=np.array(X_test_list).T
Y_test=np.array(Y_test_list)
Y_test=np.reshape(Y_test,(len(Y_test),1)).T

Y_test, d = model.model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False)
Y_test=np.array(Y_test).tolist()
Y_test1 = Y_test[0]

for i in range(len(Y_test1)):

    cur.execute("UPDATE words SET word_level = ? WHERE id = ?", (int(Y_test1[i]), (i+1),))
    con.commit()

cur.close()
con.close()
