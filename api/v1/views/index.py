#!/usr/bin/python3
""""Index module for the API"""

from flask import Blueprint, jsonify
from models import storage

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/status', strict_slashes=False)
def get_status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count_objs():
    """Retrieves the number of each objects by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
