"""Funciones de utilidad"""
from typing import Dict
import uvicorn


def run_server():
    """Corre el servidor API"""
    uvicorn.run(
        "app.main:app", reload=True, workers=2, host="0.0.0.0", port=8000
    )


def fix_mongo_id_model(model: Dict) -> Dict:
    fixed_id = str(model["_id"])
    del model["_id"]
    model["id"] = fixed_id
    return model
