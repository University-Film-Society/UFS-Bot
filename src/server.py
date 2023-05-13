from flask import Flask
from threading import Thread

app = Flask('') # Create web server

@app.route('/')
def home(): # Web Server home
  return "Hello. I am alive!"

def run(): # Run web server
  app.run(host='0.0.0.0', port=8080)

def keep_alive(): # Keeps bot running
  t = Thread(target=run)
  t.start()