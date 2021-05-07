#!/usr/bin/python3
"""Setting up API for HBNB"""
from flask import Flask, escape, request, render_template, Blueprint
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.registar_blueprint(app_views)


@app.teardown_appcontext
def teardown(context):
    """ runs when app is done"""
    storage.close()


if __name__ == "__main__":
    our_host = getenv('HBNB_API_HOST')
    our_post = getenv('HBNB_API_PORT')
    if our_host is None:
        our_host = '0.0.0.0'
    if our_post is None:
        our_post = '5000'
    app.run(host=our_host, port=our_port, threaded=True)
