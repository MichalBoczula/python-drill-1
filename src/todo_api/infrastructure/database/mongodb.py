"""Async MongoDB setup; lifespan owns the client."""

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from todo_api.infrastructure.config import Settings


def create_client(settings: Settings) -> AsyncMongoClient:
    return AsyncMongoClient(settings.mongodb_uri, serverSelectionTimeoutMS=3000)


def get_database(client: AsyncMongoClient, settings: Settings) -> AsyncDatabase:
    return client[settings.mongodb_database]
