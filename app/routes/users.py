""" Endpoints CRUD para la gestion de usuarios"""

from http import HTTPStatus
from typing import Union
from fastapi import APIRouter, Body, Query
from fastapi.responses import JSONResponse

from app.models.response import (
    ErrorResponseModel,
    ResponseModel,
    error_response_model,
    get_response_model,
)
from app.models.users import UpdateUserSchema, UserSchema
from app.repository import users
from app.repository.users import UpdateError

router = APIRouter()


@router.post(
    "/",
    response_description="User data added into the database",
    status_code=HTTPStatus.CREATED,
    response_model=ResponseModel,
)
async def add_new_user(user: UserSchema = Body(...)):
    """Endpoint para añadir usuario"""
    new_user = await users.add(user)
    return get_response_model(
        data=new_user,
        message="User add successfully",
        status=HTTPStatus.CREATED,
    )


@router.get(
    "/",
    response_description="List all users in database",
    response_model=ResponseModel,
    status_code=HTTPStatus.OK,
)
async def get_all_users():
    """Obtiene todos los usuarios listados en base de datos"""
    user_list = await users.get_all()
    return get_response_model(
        user_list, "Getting all users successfully", HTTPStatus.OK
    )


@router.get(
    "/{id_}",
    response_description="Get a single user by id",
    response_model=Union[ResponseModel, ErrorResponseModel],
    status_code=HTTPStatus.OK,
)
async def get_user_by_id(id_: str = Query(...)):
    """Getting a single user by id"""
    user = await users.get_by_id(id_)
    if user:
        return get_response_model(user, "", HTTPStatus.OK)
    return JSONResponse(
        error_response_model(
            code=HTTPStatus.NOT_FOUND, error="ID not found", message=""
        ),
        status_code=HTTPStatus.NOT_FOUND,
    )


@router.put(
    "/{id_}",
    response_description="User data for update",
    status_code=HTTPStatus.OK,
    response_model=Union[ResponseModel, ErrorResponseModel],
)
async def update_user_by_id(
    id_: str = Query(...), user: UpdateUserSchema = Body(...)
):
    """Endpoint para añadir usuario"""
    try:
        updated_user = await users.update(id_, user)
        if updated_user:
            return get_response_model(
                data=updated_user,
                message="User updated successfully",
                status=HTTPStatus.OK,
            )
    except UpdateError as e:
        return error_response_model(
            e.args[0], HTTPStatus.BAD_REQUEST, "An error has ocurred"
        )


@router.delete(
    "/{id}",
    response_description="ID user for been deleted",
    status_code=HTTPStatus.NO_CONTENT,
)
async def delete_user_by_id(id_: str = Query(...)):
    """Eliminar un usuario por su de id"""
    await users.delete_by_id(id_)
    return {}
