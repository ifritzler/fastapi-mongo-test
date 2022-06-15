"""Api con mongodb"""

from http import HTTPStatus

from dotenv import load_dotenv
from fastapi import FastAPI

from app.helpers import run_server
from app.routes.users import router as user_router

load_dotenv()

app = FastAPI()
app.include_router(user_router, tags=["Users"], prefix="/users")


@app.get("/", status_code=HTTPStatus.OK, tags=["Root"])
def hello_api():
    """Hola Mundo"""
    return {
        "message": "Welcome to the fastapi-mongo-test API, this is a "
        + "test for user mongodb database and probably"
        + " been part of an web application",
        "public_endpoints": {
            "users": {
                "root_endpoint": "/users",
                "get_all": {
                    "method": "GET",
                    "params": None,
                    "path": "/",
                    "body": None,
                    "headers": None,
                    "full_path": "/users/",
                },
                "get_by_id": {
                    "method": "GET",
                    "params": {"id": "str"},
                    "path": "/{id}",
                    "body": None,
                    "headers": None,
                    "full_path": "/users/{id}",
                },
                "add_new_user": {
                    "method": "POST",
                    "params": {"id": "str"},
                    "body": "UserSchema",
                    "headers": None,
                    "path": "/",
                    "full_path": "/users/",
                },
                "update_user": {
                    "method": "PUT",
                    "params": {"id": "str"},
                    "body": "UpdateUserSchema",
                    "headers": None,
                    "path": "/",
                    "full_path": "/users/",
                },
                "delete_user_by_id": {
                    "method": "DELETE",
                    "params": {"id": "str"},
                    "body": None,
                    "headers": None,
                    "path": "/",
                    "full_path": "/users/{id}",
                },
            },
        },
    }


if __name__ == "__main__":
    run_server()
