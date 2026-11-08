"""Explicit domain-to-document mapping."""

from uuid import UUID

from todo_api.domain.entities.task import Task
from todo_api.infrastructure.documents.task_document import TaskDocument


def to_document(task: Task) -> TaskDocument:
    return {"_id": str(task.id), "title": task.title, "completed": task.completed}


def to_domain(document: TaskDocument) -> Task:
    return Task(
        id=UUID(document["_id"]),
        title=document["title"],
        completed=document["completed"],
    )
