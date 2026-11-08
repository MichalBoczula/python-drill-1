"""MongoDB adapter skeleton, to be completed during CRUD drills."""

from pymongo.asynchronous.database import AsyncDatabase


class MongoTaskRepository:
    def __init__(self, database: AsyncDatabase) -> None:
        self._collection = database["tasks"]

    # Drill: implement the TaskRepository Protocol using Async PyMongo.
