import firebase_admin
from firebase_admin import credentials, auth
from functools import wraps
from flask import request, jsonify

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def is_authenticated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        authorization = request.headers.get("authorization")

        if not authorization:
            return jsonify({
                "status": "Bad Request",
                "message": "No token provided."
            }), 400

        if (authorization.startswith("Bearer ")):
            id_token = authorization.split("Bearer ")[1]

            try:
                decoded_token = auth.verify_id_token(id_token)
                request.current_user = decoded_token
            except Exception as e:
                return jsonify({
                    "status": "Unauthorized",
                    "message": "You do not have permissions to access the service."
                }), 401

        return func(*args, **kwargs)

    return wrapper