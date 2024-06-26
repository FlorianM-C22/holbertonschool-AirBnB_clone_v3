#!/usr/bin/python3
"""Index module for AirBnB clone API v1"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", strict_slashes=False)
def display_status():
    """returns a JSON"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def numbers_of_objs():
    """Retrieves the number of each objects by type"""
    obj_list = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
        }
    return jsonify(obj_list)
