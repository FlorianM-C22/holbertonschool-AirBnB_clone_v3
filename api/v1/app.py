#!/usr/bin/python3
"""API module"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """Handling 404 error"""
    return jsonify(error="Not found"), 404


@app.teardown_appcontext
def teardown(self):
    """Closes the storage"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
