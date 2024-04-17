#!/usr/bin/python3
"""Amenity API views"""

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage


@app_views.route("/amenities", methods=["GET"], strict_slashes=False)
def get_amenities():
    """Retrieve the list of all amenities"""
    amenities = storage.all(Amenity).values()
    amenities_dict = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenities_dict)


@app_views.route(
        "/amenities/<amenity_id>", methods=["GET"], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieve an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route(
        "/amenities/<amenity_id>", methods=["DELETE"], strict_slashes=False)
def delete_amenity(amenity_id):
    """Delete an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def create_amenity():
    """Create a new Amenity object"""
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route(
        "/amenities/<amenity_id>", methods=["PUT"], strict_slashes=False)
def update_amenity(amenity_id):
    """Update an Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200