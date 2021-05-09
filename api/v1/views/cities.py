#!/usr/bin/python3
"""Create a new view for State objects that handles all
default RestFul API actions"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
from models.city import City
import json


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def cities_by_state(state_id):
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    city_list = []
    for city in storage.all('City').values():
        if(city.state_id == states_id):
            city_list.append(city.to_dict())
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'])
def cities_id(city_id):
    """Retrieves the list of all State objects"""
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())
