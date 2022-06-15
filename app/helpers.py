"""Funciones de utilidad"""
from typing import Dict

import uvicorn
from pydantic import BaseModel


def run_server():
    """Corre el servidor API"""
    uvicorn.run(
        "app.main:app", reload=True, workers=2, host="0.0.0.0", port=8000
    )


def fix_mongo_id_model(model: Dict) -> Dict:
    """Arregla la falta de compatibilidad de ObjectID en pydantic"""
    fixed_id = str(model["_id"])
    del model["_id"]
    model["id"] = fixed_id
    return model


def return_not_none_dict_attrs(data: BaseModel):
    """
    Para las acciones PUT donde algunos valores vienen null o None, esta funcion permite quedarse
    con todos los items de un dict que no sean nulos para efectuar la operacion de update de
    forma correcta
    """
    new_data = {k: v for k, v in data.dict().items() if v is not None}
    return new_data
