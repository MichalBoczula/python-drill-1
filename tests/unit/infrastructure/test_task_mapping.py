"""Mongo mapping must preserve domain data and UUIDs."""

from uuid import uuid4

import pytest

from todo_api.domain.entities.task import Task
from todo_api.infrastructure.mapping.task_mapping import to_document, to_domain


@pytest.mark.unit
def test_task_document_roundtrip() -> None:
    original = Task(id=uuid4(), title="Write tests", completed=True)
    result = to_domain(to_document(original))

    assert result == original
