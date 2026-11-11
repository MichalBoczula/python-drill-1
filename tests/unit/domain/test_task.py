# """Pure domain tests: no MongoDB or HTTP."""

# from uuid import uuid4

# import pytest

# from todo_api.domain.entities.task import Task


# @pytest.mark.unit
# def test_new_task_is_not_completed_by_default() -> None:
#     task = Task(id=uuid4(), title="Learn Python")

#     assert task.title == "Learn Python"
#     assert task.completed is False
