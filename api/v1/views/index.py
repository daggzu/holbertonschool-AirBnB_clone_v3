#!/usr/bin/python3
"""Index view for api.v1.views"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review


# Task 4 - Create a route that returns a JSON
@app_views.route('/status', strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"})
# Task 4 - End


# Task 5 - Endpoint retrieves number of each objects by type
@app_views.route('/stats', strict_slashes=False)
def stats():
    """Return stats"""
    return jsonify({"amenities": storage.count(Amenity),
                    "cities": storage.count(City),
                    "places": storage.count(Place),
                    "reviews": storage.count(Review),
                    "states": storage.count(State),
                    "users": storage.count(User)})
# Task 5 - End
