#!/usr/bin/python3

import json
import random
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return '<a href="jays_poems">jays poems</a>'

@app.route("/jays_poems", defaults={'pn':'batman'})
@app.route("/jays_poems/<pn>")
def send(pn):
    if pn == "batman":
        pn = str(random.randrange(1, 5, 1))
    with open('poems.json') as jp:
        jp = json.load(jp)
    if jp.get(pn):
        return jp.get(pn)
    else:
        return "the key does not exist"

if __name__ == '__main__':
    app.run(port=5006)