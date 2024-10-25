from flask import Response, Request, Blueprint, request, jsonify, make_response
from flask_login import login_required, current_user
from sqlalchemy import inspect

from backend.models.engine import db_session
from backend.models.models import *

import logging

api_view = Blueprint('api', __name__, url_prefix="/api")


@api_view.route("/get/<path>", methods=["GET"])
@login_required
async def get_obj(path: str) -> Response:
    model = eval(path)
    with (db_session() as db):
        try:
            tables = [model]
            objs = db.query(model)
            """for rel in inspect(model).relationships:
                                       if rel.secondary is not None and rel.backref is not None:
                                           tables.append(rel.mapper.class_)
                                           objs = objs.join(rel.mapper.class_)"""
            for table in tables:
                for key, value in request.args.items():
                    positive = True
                    if key.find("not_") == 0:
                        key = key.replace("not_", "")
                        positive = False
                    if hasattr(table, key):
                        attr = getattr(table, key)
                        value = None if value in ("None", "null", "") else value
                        objs = objs.filter(attr == attr.type.python_type(value)) if positive else objs.filter(
                                attr != value)
            limit = request.args.get("limit") if "limit" in request.args.keys() else 50
            offset = request.args.get("offset") if "offset" in request.args.keys() else 0
            objs = objs.limit(limit).offset(offset).all()
            node = {"result": [obj.to_dict() for obj in objs]}
            node['result'] = sorted(node['result'], key=lambda it: it[inspect(model).primary_key[0].name])
            response = jsonify(node)
            response.headers.add("Access-Control-Allow-Origin", "*")
        except Exception as e:
            response = jsonify({"result": "error!", "message": str(e)})
            response.status = 500
            logging.error(
                    f"error! message - {str(e)} traceback - {str(e.__traceback__.tb_lineno)} {str(e.__traceback__.tb_frame.f_code.co_name)}")
    return response
