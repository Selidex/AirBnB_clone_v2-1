#!/usr/bin/python3
""" This is an init file, not exactly sure what is happening in here
just yet """
from flask import Blueprint

app_view = Blueprint('app_view', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
