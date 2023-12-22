#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

# Task 4 - Create an instance of Flask
app = Flask(__name__)
app.register_blueprint(app_views)  # Register Blueprint with Flask app
# Task 13 - Flask-Cors
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})
# Task 13 - End


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


# Task 6 - Error handler
@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 error"""
    return jsonify({"error": "Not found"}), 404
# Task 6 - End


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
# Task 4 - End
