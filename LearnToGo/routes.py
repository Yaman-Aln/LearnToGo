#python3
#where the user inputted words are routed in to the right table
#whether it is a single word or a paragraph the user enters.

#note, often using the same imports all across as this has been recently modulated. Requires cleaning.
import math #to allow for truncating
import requests #to get data from website
from flask import Flask, render_template, request, Blueprint #to render the html template (has to be in a folder), and to request certain cell data in db
from flask_sqlalchemy import SQLAlchemy
import csv #using this to import the main file with words/translated words/features
import sqlite3 #for using the .connect
from . import db
from LearnToGo.models import Words
from LearnToGo import data_import
from LearnToGo.config import Config #importing configuration of db.
#from LearnToGo.logistic_regression import testdata_accuracy #This shows accuracy of log_reg on training model
#from LearnToGo.logistic_regression import model_run #runs trained model on saved words in db to assign levels 0 (beginner) or 1 (non-beginner)
from LearnToGo.matching_algorithm import matching #instead of log_reg uses library matching algorithm (as well as personally developed if statements) to assign levels 1-5
from LearnToGo.logistic_regression import top_ten

main = Blueprint('main', __name__)

@main.route ('/', methods=['GET','POST'])

def home():
    #references data_import file to insure those tables are populated prior to population of words
    data_import
    con = sqlite3.connect('/Users/yaman/Downloads/Programming/Backend/venv/LearnToGo/LearnToGo/words.db')
    #if there is data in the textbox
    if request.form:
        key_words=request.form.get("key_words", None)
        key_words = key_words.lower()
        key_words = key_words.strip()
        #if there is more than one word
        if len(key_words.split())>1:
            #can use re expression
            par= key_words.replace('\n', '').replace('\r', ' ').split(' ')
            while '' in par:
                par.remove('')
            print(par)
        #want to extract each word onto a new line
            for word in par:
                #Could use Levenshtein approximation algoirthm or Jaro–Winkler ie fuzzy string for words that
                #should have been incorporated but are currently not. Instead just stripping.
                word = word.strip('\r')
                word = word.strip('\n')
                print(word)
                word = word.strip('""  ,-.!&?()$ ')
                cur = con.cursor()
                #check if it already exists in the table
                cur.execute("""SELECT key_words FROM words WHERE key_words = ?""", (word,))
                exists = cur.fetchone()
                if exists is None:
                    print(word)
                    cur.execute("""SELECT word_length, word_syllables, word_usage_rank FROM english_dict WHERE english_dict.word_original = ?""", (word,))
                    length_of_word, syllables_of_words, usage_of_words = cur.fetchone()[0], cur.fetchone()[1], cur.fetchone()[2]
                    sqlite_insert_query = """INSERT INTO `words`
                                       ('key_words', 'word_length', 'word_syllables', 'word_usage_rank')
                                        VALUES
                                       (?,?, ?, ?)"""
                    count = cur.execute(sqlite_insert_query,(word, length_of_word, syllables_of_words, usage_of_words))
                    con.commit()

        else:
            word = key_words
            #Could use Levenshtein approximation algoirthm or Jaro–Winkler for words that
            #should have been incorporated but are currently not. Instead just stripping.
            word = word.strip(""',-.!&?()$ ')
            cur = con.cursor()
            cur.execute("""SELECT key_words FROM words WHERE key_words = ?""", (word,))
            exists = cur.fetchone()
            if exists is None:
                print(word)
                cur.execute("""SELECT word_length, word_syllables, word_usage_rank FROM english_dict WHERE english_dict.word_original = ?""", (word,))
                length_of_word, syllables_of_words, usage_of_words = cur.fetchone()[0],cur.fetchone()[1], cur.fetchone()[2]
                sqlite_insert_query = """INSERT INTO `words`
                                   ('key_words', 'word_length', 'word_syllables', 'word_usage_rank')
                                    VALUES
                                   (?,?,?,?)"""
                count = cur.execute(sqlite_insert_query,(word, length_of_word, syllables_of_words, usage_of_words))
                con.commit()
    #cur.close()
    algorithm =request.form.get("algorithm", None)
    level =request.form.get("level", None)
    print("This is routes", algorithm, level)
    #model_run
    #testdata_accuracy
    matching
    top_ten_words = top_ten.top(algorithm, level)
    con.close()
    return render_template("LearnToGo.html", top_ten= top_ten_words)
