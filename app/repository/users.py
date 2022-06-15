from typing import List
from bson.objectid import ObjectId
from app.helpers import fix_mongo_id_model
from app.database import user_collection


async def get_all() -> List:
    """Devuelve los usuarios de la base de datos mongo"""
    users = []
    async for user in user_collection.find():
        users.append(fix_mongo_id_model(user))
    return users


async def add(user_data: dict) -> dict:
    """Crea y devuelve el nuevo usuario generado"""
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return fix_mongo_id_model(new_user)


async def get_by_id(id_: str):
    """Busca una coincidencia en la bd por id"""
    user = await user_collection.find_one({"_id": ObjectId(id_)})
    if user:
        return fix_mongo_id_model(user)
    return None


async def update(id_: str, data: dict):
    """Actualiza un usuario"""
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id_)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id_)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


async def delete_by_id(id_: str):
    """Elimina un usuario por su id"""
    user = await user_collection.find_one({"_id": ObjectId(id_)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id_)})
        return True
    return False
