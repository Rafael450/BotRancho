from flask import request
from mod_read import create_app
import mod_read.tweet as tweet

app = create_app()

@app.route('/')
def hello_world():
    if request.method == 'HEAD':
        tweet.time_checker()
    
    return 'Hello World!' 

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
    