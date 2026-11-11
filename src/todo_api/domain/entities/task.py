from dataclasses import dataclass
from uuid import UUID
from ..common.enums.task_status import TaskStatus


@dataclass(slots=True)
class ToDoTask:
    id: UUID
    name: str
    state: TaskStatus

    def changeStatus(self, new_state: TaskStatus) -> None:
        self.state = new_state
