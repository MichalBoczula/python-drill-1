"""Task document representation; not part of Domain."""

from typing import TypedDict


class TaskDocument(TypedDict):
    _id: str
    title: str
    completed: bool
