from app import keep_alive 
import requests
import schedule
import time

def send_request():
    URL = "https://github-readme-activity-graph.ritabratadas1.repl.co"
    r = requests.get(url = URL)
    print(r)

keep_alive()

schedule.every(5).seconds.do(send_request)

while True:
	schedule.run_pending()
	time.sleep(1)
