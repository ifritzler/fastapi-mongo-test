""" Models for response consistency """

from typing import List

from pydantic import BaseModel


class ResponseModel(BaseModel):
    """Modelo de respuesta para el envio de datos al front"""

    data: List
    code: int
    message: str


class ErrorResponseModel(BaseModel):
    """Modelo de respuesta para el envio de datos al front"""

    error: str
    code: int
    message: str


def get_response_model(data, message, status):
    """Basic response model"""
    return {
        "data": [data],
        "code": status,
        "message": message,
    }


def error_response_model(error, code, message):
    """Basic response model in errors"""
    return {
        "error": error,
        "code": code,
        "message": message,
    }
