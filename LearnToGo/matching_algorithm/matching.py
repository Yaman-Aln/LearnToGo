#again, recently modulated, imports require cleaning

import numpy as np #library
import matplotlib.pyplot as plt
import os #helps with interface on terminal
import pandas as pd #library
import csv
import sqlite3

#function uses weights to determine levels. In this program, is used as a back-up when
#there is no "given" value for the words typed by user.

def level_algorithm(word):
    cur.execute("SELECT word_length, word_syllables, word_usage_rank FROM words WHERE key_words = ?", (word,))
    word_features = cur.fetchone()
    word_length, word_syllables, word_usage = word_features[0], word_features[1], word_features[2]

    weight_score = 0
    word_level = 0

    if word_length <= 3:
        weight_score+= 0
    elif word_length >= 4 and word_length < 6 :
        weight_score+= 1
    elif word_length >=6 and word_length <9:
        weight_score+= 3
    else:
        weight_score+= 5
    if word_syllables == 1:
        weight_score+= 0
    elif word_syllables ==2 :
        weight_score+= 3
    elif word_syllables == 3:
        weight_score+= 5
    else:
        weight_score+= 5
    if word_usage <= 1000:
        weight_score+= 0
    elif word_usage >=1001 and word_usage <= 2000:
        weight_score+= 1
    elif word_usage >= 2001 and word_usage <=5000:
        weight_score+= 3
    elif word_usage >= 5001 and word_usage <=10000:
        weight_score+= 5
    elif word_usage >= 10001 and word_usage <=20000:
        weight_score+= 7
    else:
        weight_score+= 9
    if weight_score <=3:
        word_level = 1
    elif weight_score >= 4 and weight_score <6:
        word_level = 2
    elif weight_score >= 6 and weight_score < 10:
        word_level = 3
    elif weight_score >= 10 and weight_score <=13:
        word_level = 4
    else:
        word_level = 5
    return word_level


#primary reference is the langapp_train, if word is not there use above function
con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
cur = con.cursor()
word =[]
level = []

for row in cur.execute("SELECT key_words FROM words"):
    word.append(row[0])

for i in range(len(word)):
    try:
        cur.execute("SELECT word_level FROM langapp_train WHERE word_original = ?", (word[i],))
        trial = cur.fetchone()
        level.append(int(trial[0]))

    except:
        level.append(level_algorithm(word[i]))

#updates words table in the db to match te right level 
for i in range(len(word)):
    cur.execute("UPDATE words SET word_level = ? WHERE key_words = ?", (level[i], word[i],))
    trial = cur.fetchone()
    con.commit()

cur.close()
con.close()
