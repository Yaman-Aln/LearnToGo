"""
#the intent of this module is to find the top 10 words a user should learn in the article.
    #1 option: want the most common words in the article at that level frequency wise (which means we need a column with a counter)
    #2 option: want the words that are most used in the english language that are also used even once in the script
        #easiest with as is code
        #argument can be made that poeple should learn these words since they overlap with other
    #3 option: weighted formula
    #I am choosing option 2, my decision is guided by most transferrable words to conversation
Input: the level as well as the words table
Output: top 10 words to learn
@author: yaman
"""
#again, modulated recently, imports need cleanup
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import csv
import sqlite3
import requests #to get data from website
from flask import Flask, render_template, request, Blueprint

#main = Blueprint('main', __name__)

#@main.route ('/', methods=['GET','POST'])
#def home():
#print(level)
#print(algorithm)

def top(algorithm, level):
    if level:
        print("Hello! This is top_ten")
        con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
        cur = con.cursor()
        print("This is top", algorithm, level)
        top_10_words =[]
        top_10_id = []
        word_id=[]
        words_list=[]
        word_usage=[]
        print(level)
        #def top_10_sort:

        if algorithm == "log_reg":
            if level == 1:
                for row in cur.execute("SELECT id, key_words, word_usage_rank FROM words WHERE word_level = 0"):
                    word_id.append(row[0])
                    words_list.append(row[1])
                    word_usage.append(row[2])
                #negate an array, the lowest elements become the highest elements, last 10 elements
                #Instead of negating argsort(-word_usage), note efficience of following: O(n log n) in time complexity, because the argsort call is the dominant term here. But the second approach has a nice advantage: it replaces an O(n) negation of the array with an O(1) slice. If you're working with small arrays inside loops then you may get some performance gains from avoiding that negation, and if you're working with huge arrays then you can save on memory usage because the negation creates a copy of the entire array.
                #Could have sorted along array as opposed to these lists
                top_10_index = np.argsort(word_usage)[::-1][-10:]
                for i in top_10_index:
                    top_10_words.append(words_list[i])
                    top_10_id.append(word_id[i])
            else:
                for row in cur.execute("SELECT id, key_words, word_usage_rank FROM words WHERE word_level = 1"):
                    word_id.append(row[0])
                    words_list.append(row[1])
                    word_usage.append(row[2])
                top_10_index = np.argsort(word_usage)[::-1][-10:]
                for i in top_10_index:
                    top_10_words.append(words_list[i])
                    top_10_id.append(word_id[i])
        else:
            level = int(level) + 1
            print("The level is matching: ", level)
            for row in cur.execute("SELECT id, key_words, word_usage_rank FROM words WHERE word_level = ?", (level,)):
                word_id.append(row[0])
                words_list.append(row[1])
                word_usage.append(row[2])
            #negate an array, the lowest elements become the highest elements, last 10 elements
            #Instead of negating argsort(-word_usage), note efficiency of following: O(n log n) in time complexity, because the argsort call is the dominant term here. But the second approach has a nice advantage: it replaces an O(n) negation of the array with an O(1) slice. If you're working with small arrays inside loops then you may get some performance gains from avoiding that negation, and if you're working with huge arrays then you can save on memory usage because the negation creates a copy of the entire array.
            #Could have sorted along array as opposed to these lists
            top_10_index = np.argsort(word_usage)[::-1][-10:]
            for i in top_10_index:
                top_10_words.append(words_list[i])
                top_10_id.append(word_id[i])


        print(top_10_words)
        return top_10_words
    return ''
    #elif algorithm == "match_alg":
