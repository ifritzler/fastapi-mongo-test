"""Api con mongodb"""

from http import HTTPStatus

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.helpers import run_server
from app.routes.users import router as user_router

load_dotenv()

app = FastAPI()
app.include_router(user_router, tags=["Users"], prefix="/users")


@app.get("/{name}", status_code=HTTPStatus.OK, tags=["Root"])
def hello(name: str = "Mundo"):
    """Hola Mundo"""
    return JSONResponse(
        content={"msg": f"Hola {name}!", "status": HTTPStatus.OK}
    )


if __name__ == "__main__":
    run_server()
