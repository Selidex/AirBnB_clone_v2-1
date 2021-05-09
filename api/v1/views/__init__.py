#!/usr/bin/python3
""" This is an init file, not exactly sure what is happening in here
just yet """
from flask import Blueprint

app_views = Blueprint('app_view', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
