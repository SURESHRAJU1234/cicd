import platform
from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    message = "MK:You did it. Welcome to Hello world of Kubernetes demo "+platform.node() + ". Current time is " +date_time
    return message

if __name__ == "__main__":
    app.run(host='0.0.0.0')
