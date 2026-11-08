"""The application service. Implement the use cases during drills."""

from todo_api.domain.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    # Drill: implement create, get, list, update and delete here.
