""" database init """

import os
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    os.getenv("MONGO_DB_URI") or "mongodb://localhost:27017"
)

database = client.test_database
user_collection = database.get_collection("users")
