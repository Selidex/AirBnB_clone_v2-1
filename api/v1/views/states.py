#!/usr/bin/python3
"""Create a new view for State objects that handles all
default RestFul API actions"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'])
def states():
    """Retrieves the list of all State objects"""
    obj_list = []
    for state in storage.all('State').values():
        obj_list.append(state.to_dict())
    return jsonify(obj_list)


@app_views.route('/states/<state_id>', methods=['GET'])
def states_id(state_id):
    """Retrieves the list of all State objects"""
    obj_dict = storage.get(State, state_id)
    if obj_dict is None:
        abort(404)
    return jsonify(obj_dict.to_dict())
