import json
import os
import datetime
import random
import requests

from flask import Flask
app = Flask(__name__)

quotes = requests.get("https://raw.githubusercontent.com/kidd/quotes/master/bin/quotes.txt").text.splitlines()

@app.route("/reload")
def load():
    quotes = requests.get("https://raw.githubusercontent.com/kidd/quotes/master/bin/quotes.txt").text.splitlines()

@app.route("/")
def hello():
    return random.sample(quotes, 1)[0]

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
