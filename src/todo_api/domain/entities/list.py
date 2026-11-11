from dataclasses import dataclass, field
from uuid import UUID
from .task import ToDoTask
from ..common.enums.task_status import TaskStatus


@dataclass(slots=True)
class ToDoList:
    id: UUID
    title: str
    state: TaskStatus
    description: str | None
    complete: bool = False
    tasks: list[ToDoTask] = field(default_factory=list)

    def change_state(self, new_state: TaskStatus) -> None:
        self.state = new_state
