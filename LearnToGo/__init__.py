#python3

import math #to allow for truncating - leftover from when this was non-modulated. Leaving in to make a point.
import requests #to get data from website - leftover from when this was non-modulated. Leaving in to make a point.
from flask import Flask, render_template, request #to render the html template (has to be in a folder), and to request certain cell data in db
from flask_sqlalchemy import SQLAlchemy #toolkit to help with SQLite db
import csv #using this to import the main file with words/translated words/features
import sqlite3 #for using the .connect
from LearnToGo.config import Config #importing configuration of db.
#from LearnToGo.logistic_regression import testdata_accuracy #This shows accuracy of log_reg on training model
#from LearnToGo.logistic_regression import model_run #runs trained model on saved words in db to assign levels 0 (beginner) or 1 (non-beginner)
#from LearnToGo.matching_algorithm import matching #instead of log_reg uses library matching algorithm (as well as personally developed if statements) to assign levels 1-5
#from LearnToGo.logistic_regression import top_ten

#creating object to be configured
db = SQLAlchemy()

algorithm = 0
level = 0
#configuring db:
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from LearnToGo.routes import main
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()
    print("Heck", algorithm, level)
    return app
#different modules to refer to depending on use-case
# app = Flask(__name__)
# with app.app_context():
#     print("No", algorithm, level)
#     algorithm =request.form.get("algorithm", None)
#     level =request.form.get("level", None)
print(algorithm, level)
