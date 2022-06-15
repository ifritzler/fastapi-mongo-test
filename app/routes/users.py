from http import HTTPStatus
from fastapi import APIRouter, Body, Query
from fastapi.encoders import jsonable_encoder

from app.models.response import error_response_model, response_model
from app.models.users import UpdateUserModel, UserSchema
from app.repository import users


router = APIRouter()


@router.post(
    "/",
    response_description="User data added into the database",
    status_code=HTTPStatus.CREATED,
)
async def add_new_user(user: UserSchema = Body(...)):
    """Endpoint para añadir usuario"""
    user = jsonable_encoder(user)
    new_user = await users.add(user)
    return response_model(
        data=new_user,
        message="User add successfully",
        status=HTTPStatus.CREATED,
    )


@router.put(
    "/{id_}",
    response_description="User data for update",
    status_code=HTTPStatus.OK,
)
async def update_user(
    id_: str = Query(...), user: UpdateUserModel = Body(...)
):
    """Endpoint para añadir usuario"""
    user = {k: v for k, v in user.dict().items() if v is not None}
    user = jsonable_encoder(user)
    updated_user = await users.update(id_, user)
    if updated_user:
        return response_model(
            data=[], message="User updated successfully", status=HTTPStatus.OK
        )
    return error_response_model(
        "An error ocurred", 404, "There was an error updating the user data"
    )
