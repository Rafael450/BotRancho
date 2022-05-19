import datetime
import openpyxl
import config
from flask import request, Blueprint
from mod_read.models import db
from mod_read.models import WeekDay
import json

mod_read = Blueprint('read', __name__, url_prefix='/read')

@mod_read.route('/upload', methods = ['POST'])
def upload_file():
    input_password = request.form['password']
    if input_password == config.PASSWORD:
        db.drop_all()
        db.create_all()
        f = request.files['file']
        wb = openpyxl.load_workbook(f)
        sheet = wb.active
        table = []
        for i in range(0,7):
            row = []
            table.append(row)
            for j in range(0,4):
                table[i].append(sheet.cell(row=i+3, column=j+2).value)
            day = WeekDay(table[i][0], table[i][1], table[i][2], table[i][3])
            db.session.add(day)
        db.session.commit()
        
        return json.dumps({'message':'File uploaded successfully','status':200}),200 
    else:
        return json.dumps({'message':'Incorrect password','status':401}),401 


def read_meal(meal):
    #considerar meal = 1 para almoço e meal = 2 para janta
    day = datetime.datetime.today().weekday()    
    weekmeal = WeekDay.query.filter_by(day=day+1).first()
    if meal == 1:
        proteina = weekmeal.lunch1
        massa = weekmeal.lunch2
    else:
        proteina = weekmeal.dinner1
        massa = weekmeal.dinner2
    
    print([proteina, massa])
    return [proteina, massa]

