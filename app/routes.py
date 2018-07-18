#need to import app variable
import os
from app import app
#if you want to render html
from flask import render_template, url_for, jsonify, request
import json
import requests



@app.route('/')
@app.route('/index')
def index():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "assets", "items.json")
    with open(json_url) as items:
        data = items
    # url = "http://127.0.0.1:5000/"
    # value = requests.get(url).json()
    return render_template('index.html',data=data)
