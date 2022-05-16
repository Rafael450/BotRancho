import sys
import config
from flask import Flask, request
from flask_apscheduler import APScheduler
import create
import json

app = Flask(__name__)
scheduler = APScheduler()

@app.route('/upload', methods = ['POST'])
def upload_file():
    input_password = request.get_json()['password']
    if input_password == config.PASSWORD:
        f = request.files['file']
        f.save('cardapio.xlsx')
        return json.dumps({'message':'File uploaded successfully','status':200}),200 
    else:
        return json.dumps({'message':'Incorrect password','status':401}),401 

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func=create.time_checker, trigger="interval", seconds=3)
    scheduler.start()
    app.run(host='localhost', port=8080, debug=True)