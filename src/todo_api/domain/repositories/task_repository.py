"""The persistence port to implement during CRUD drills."""

from typing import Protocol
from uuid import UUID

from todo_api.domain.entities.task import Task


class TaskRepository(Protocol):
    async def add(self, task: Task) -> None: ...

    async def get_by_id(self, task_id: UUID) -> Task | None: ...

    async def list_all(self) -> list[Task]: ...
