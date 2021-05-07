#!/usr/bin/python3
"""Create an endpoint that retrieves the number of each objects by type"""
from api.v1.views import app_views
from flask import jsonify
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app_views.route('/status')
def status():
    """Returns Status:OK"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    """Returns Status:OK"""
    obj_dict = {}
    for obj in classes:
        obj_dict[obj] = storage.count(classes[obj])
    return jsonify(obj_dict)
