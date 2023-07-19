#!/usr/bin/env python3
"""A web server using Flask and api.v1.views blueprint."""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
app = Flask(__name__)
app.register_blueprint(app_views)
@app.errorhandler(404)
def not_found(error):
    """Return a JSON response with 404 status code and error message.

    Args:
        error (Exception): The error that triggered the handler.
    """
    return jsonify({"error": "Not found"}), 404)
if __name__ == "__main__":

    """Run the web server on host 0.0.0.0 and port 5000.

    Usage: python -m api.v1.app
    """
     app.run(host="0.0.0.0", port=5000)

