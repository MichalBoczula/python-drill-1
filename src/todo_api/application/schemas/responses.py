"""HTTP response DTOs."""

from uuid import UUID

from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: UUID
    title: str
    completed: bool
