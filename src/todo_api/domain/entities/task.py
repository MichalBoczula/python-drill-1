"""Pure-Python To-Do task entity."""

from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class Task:
    id: UUID
    title: str
    completed: bool = False
