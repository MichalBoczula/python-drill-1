"""Real MongoDB integration test using a disposable Testcontainers instance."""

from uuid import uuid4

import pytest
from pymongo import AsyncMongoClient
from testcontainers.mongodb import MongoDbContainer


@pytest.mark.integration
async def test_mongodb_can_persist_and_read_a_document() -> None:
    with MongoDbContainer("mongo:8.0") as container:
        client = AsyncMongoClient(container.get_connection_url())
        try:
            await client.admin.command("ping")
            collection = client["python_drill_integration"]["tasks"]
            document_id = str(uuid4())
            await collection.insert_one({"_id": document_id, "title": "Mongo works"})
            stored = await collection.find_one({"_id": document_id})
            assert stored is not None
            assert stored["title"] == "Mongo works"
        finally:
            await client.close()
