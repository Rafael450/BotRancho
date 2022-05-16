import sys
import config
from flask import Flask, request
from flask_apscheduler import APScheduler
import create
import json

app = Flask(__name__)
scheduler = APScheduler()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods = ['POST'])
def upload_file():
    input_password = request.form['password']
    if input_password == config.PASSWORD:
        f = request.files['file']
        f.save('cardapio.xlsx')
        return json.dumps({'message':'File uploaded successfully','status':200}),200 
    else:
        return json.dumps({'message':'Incorrect password','status':401}),401 

@app.route('/start', methods = ['POST'])
def start_app():
    print(config.IDLE_TIME)
    scheduler.add_job(id = 'Start', func=create.time_checker, trigger="interval", seconds=int(config.REPEAT_TIME))
    scheduler.start()
    

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)