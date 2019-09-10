# . is the __init__
from . import db

#create the class ie table of words user is inputting
class Words (db.Model):
    #id is the one primary_key (reference)
    id = db.Column(db.Integer, primary_key=True)
    key_words = db.Column(db.String, unique=True)
    word_length = db.Column(db.Integer)
    word_syllables = db.Column(db.Integer)
    word_usage_rank = db.Column(db.Integer)
    word_level = db.Column(db.Integer)

    def __repr__(self):
        return "<key words: {}>".format(self.key_words)
