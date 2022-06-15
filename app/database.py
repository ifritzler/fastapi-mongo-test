""" database init """

import os
import motor.motor_asyncio

MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "test_database"

if os.getenv("DEVELOPER_MODE") is False:
    MONGO_URI = os.getenv("MONGO_DB_URI")
    MONGO_DB = os.getenv("MONGO_DB_DATABASE")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

database = client[str(MONGO_DB)]
user_collection = database.get_collection("users")
