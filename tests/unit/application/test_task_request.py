"""Input validation tests, independent of FastAPI and MongoDB."""

import pytest
from pydantic import ValidationError

from todo_api.application.schemas.requests import CreateTaskRequest


@pytest.mark.unit
def test_task_title_is_trimmed() -> None:
    request = CreateTaskRequest(title="  Learn Python  ")
    assert request.title == "Learn Python"


@pytest.mark.unit
@pytest.mark.parametrize("title", ["", " ", "x" * 201])
def test_task_title_validation(title: str) -> None:
    with pytest.raises(ValidationError):
        CreateTaskRequest(title=title)
