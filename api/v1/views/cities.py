#!/usr/bin/python3
"""Cities module for AirBnB clone API v1"""

from flask import jsonify, request, abort
from models import storage
from models.city import City
from api.v1.views import app_views


@app_views.route('/cities', methods=['GET'], strict_slashes=False)
def get_cities():
    """Retrieves the list of all City objects"""
    cities = storage.all(City).values()
    if cities is None:
        abort(404)
    city_dict = []
    for city in cities:
        all_cities = city.to_dict()
        city_dict.append(all_cities)
    return jsonify(city_dict)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route(
    '/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities', methods=['POST'], strict_slashes=False)
def create_city():
    """Create a new City object"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400

    new_city = City(**data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Update a City object"""
    city_get = storage.get(City, city_id)
    if city_get is None:
        abort(404)

    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city_get, key, value)

    storage.save()
    return jsonify(city_get.to_dict()), 200
