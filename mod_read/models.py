
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from mod_read import db

class WeekDay(db.Model):
    __tablename__ = 'Semana'
    
    day = db.Column(db.Integer, primary_key=True)
    lunch1 = db.Column(db.Unicode(80, collation='pt_BR.utf8'))
    lunch2 = db.Column(db.Unicode(80, collation='pt_BR.utf8'))      
    dinner1 = db.Column(db.Unicode(80, collation='pt_BR.utf8'))
    dinner2 = db.Column(db.Unicode(80, collation='pt_BR.utf8'))
    
    def __init__(self, lunch1, lunch2,dinner1,dinner2):
        self.lunch1 = lunch1
        self.lunch2 = lunch2
        self.dinner1 = dinner1
        self.dinner2 = dinner2
        