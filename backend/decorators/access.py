from flask import jsonify
from flask_login import current_user


def has_access(func):
    def wrapper(*args, **kwargs):
        if current_user:
            func()
        else:
            return jsonify({"message": "no access"}), 401

    return wrapper
