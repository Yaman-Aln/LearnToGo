#Python3
#This is where the tables langapp_train (~2000 words grouped with their features and grouped into levels 1 to 5, used in matching algorithm
#langdata_training_logistic (~50 words with their features and assigned 0/1 for beginner/non-begnner, logistic regression traning
#and english_dict (with most english words assigned the different features)
#are created in the words.db .
#Note some features are here that are not currently used in analysis, but may be in future.

import math #to allow for truncating
import requests #to get data from website
from flask import Flask, render_template, request #to render the html template (has to be in a folder), and to request certain cell data in db
from flask_sqlalchemy import SQLAlchemy
import csv #using this to import the main file with words/translated words/features
import sqlite3 #for using the .connect
from . import db
from LearnToGo.models import Words

con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
cur = con.cursor()

#can make a method passes table name to check if it exists and if not, create it
cur.execute("""CREATE TABLE IF NOT EXISTS langapp_train (word_original, word_translation, word_length, word_syllables, word_usage_rank, word_level);""")

cur.execute("""CREATE TABLE IF NOT EXISTS langdata_training_logistic (word_length, word_syllables, word_usage_rank, word_level);""")

with open('LearnToGo/logistic_regression/langdata_training_logistic.csv','r', encoding="latin-1") as fin:
     # csv.DictReader uses first line in file for column headings by default
     #dr for DictReader
     dr_train = csv.DictReader(fin) # comma is default delimiter
     to_train_db = [(i['word_length'], i['word_syllables'], i['word_usage_rank'], i['word_level']) for i in dr_train]

cur.executemany("INSERT OR IGNORE INTO langdata_training_logistic (word_length, word_syllables, word_usage_rank, word_level) VALUES (?, ?, ?, ?);", to_train_db)

cur.execute("""CREATE TABLE IF NOT EXISTS english_dict (word_original, word_translation, word_length, word_syllables, word_usage_rank, word_level);""")

with open('LearnToGo/logistic_regression/SourceOfTruth_train.csv','r', encoding="latin-1") as fin:
    # csv.DictReader uses first line in file for column headings by default
    #dr for DictReader
    dr_train = csv.DictReader(fin) # comma is default delimiter
    to_train_db = [(i['word_original'], i['word_translation'], i['word_length'], i['word_syllables'], i['word_usage_rank'], i['word_level']) for i in dr_train]

cur.executemany("INSERT OR IGNORE INTO langapp_train (word_original, word_translation, word_length, word_syllables, word_usage_rank, word_level) VALUES (?, ?, ?, ?, ?, ?);", to_train_db)

with open('LearnToGo/logistic_regression/SourceOfTruth_dict.csv','r', encoding="latin-1") as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    #dr for DictReader
    dr_dict = csv.DictReader(fin) # comma is default delimiter
    to_dict_db = [(i['word_original'], i['word_translation'], i['word_length'], i['word_syllables'], i['word_usage_rank'], i['word_level']) for i in dr_dict]

cur.executemany("INSERT OR IGNORE INTO english_dict (word_original, word_translation, word_length, word_syllables, word_usage_rank, word_level) VALUES (?, ?, ?, ?, ?, ?);", to_dict_db)

con.commit()
con.close()
