from flask import Flask
from threading import Thread
import requests
import schedule

app = Flask('')

l = list()

def run():
    app.run(host = '0.0.0.0', port = 8080)

def keep_alive(): 
    t = Thread(target = run)
    t.start()

def send_request():
    URL = "https://github-readme-activity-graph.ritabratadas1.repl.co"
    r = requests.get(url = URL)
    l.append(str(r))

@app.route('/')
def home():
    keep_alive()
    schedule.every(5).seconds.do(send_request)
    schedule.run_pending()
    return l