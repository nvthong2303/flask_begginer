from database.db import db
from typing import Union
from models.models import User
from flask import Response, jsonify
from werkzeug.wrappers import Response as ResponseType


def ok(resource: Union[db.Model, List[db.Model]]) -> ResponseType:
    """
    Helper function that returns an http status code 200 and the
    serialized model.

    @param resource: Model or a list of models to be serialized.
    """

    if isinstance(resource, User):
        return jsonify(resource.serialize())
    return jsonify([res.serialize() for res in resource])


def no_content() -> ResponseType:
    """
    Helper function that returns an http status code 204
    """

    return Response(status=204)


def created(model: db.Model) -> ResponseType:
    """
    Helper function that returns an http status code 201 and the
    serialized model.

    @param mode: Model to be serialized
    """

    return jsonify(model.serialize()), 201


def bad_request(exception: Exception) -> ResponseType:
    """
    Helper function that return an https status code 400 and an error message.

    @params exception: the exception throwed.
    """

    return Response(response=str(exception), status=400)


def not_found(resource: str) -> ResponseType:
    """
    Helper function that return an https status code 404.

    @params resource: Resource name that was not found
    """

    return Response(response=f'{resource} not found'.capitalize(), status=404)


def not_allowed() -> ResponseType:
    """
    Helper function that return an https status code 405.

    @params: 
    """

    return Response(response='Method not allowed', status=405)


def interal_error() -> ResponseType:
    """
    Helper function that return an http status code 500.
    """

    return Response(response='Internal Error', status=500)
