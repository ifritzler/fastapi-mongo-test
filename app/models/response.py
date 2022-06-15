""" Models for response consistency """


def response_model(data, message, status):
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
