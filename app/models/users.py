"""Users model"""
from typing import Optional

from pydantic import BaseModel, Field, validator


class UserSchema(BaseModel):
    """Modelo basico de usuario para mongodb"""

    name: str = Field(...)
    lastname: str = Field(...)
    campaign: str = Field(...)
    active: Optional[bool] = Field(default=True)

    @validator("campaign")
    def campaign_must_be_correct(cls, value):
        """Valida que la campaña sea alguna de las definidas"""
        campaigns = ["reagendas", "pendiente_comercial"]
        if value not in campaigns:
            raise ValueError(
                f"Must be one of the following campaigns: {campaigns}"
            )
        return value

    class Config:
        """Extra configs"""

        schema_extra = {
            "example": {
                "name": "Ilan",
                "lastname": "Fritzler",
                "campaign": "reagendas",
                "active": "True",
            }
        }


class UpdateUserSchema(BaseModel):
    """Schema for user updates"""

    name: Optional[str]
    lastname: Optional[str]
    campaign: Optional[str]
    active: Optional[bool]

    class Config:
        """Extra configs"""

        schema_extra = {
            "example": {
                "name": "Ilan Emanuel",
                "lastname": "Fritzler",
                "campaign": "pendiente_comercial",
                "active": "True",
            }
        }
