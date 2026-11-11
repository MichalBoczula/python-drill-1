from uuid import UUID

from todo_api.application.exceptions.to_do_list_not_found_error import ToDoListNotFoundError
from todo_api.application.exceptions.validation_exception import ValidationException


class TaskService:
    repository: TaskRepository
    mapper: TaskMapper
    validator: ValidationPolicy

    def __init__(self, 
                repository: TaskRepository, 
                mapper: TaskMapper,
                validator:  ValidationPolicy
            ) -> None:
        self.repository = repository
        self.mapper = mapper
        self.validator = validator

    def get_list_by_id(self, list_id: UUID) -> ToDoListResponseDto:
        list = self.repository.getListById(id)
        if list is None:
            raise ToDoListNotFoundError()
        return list

    def create_list(self, new_list: CreateToDoListRequestDto) -> ToDoListResponseDto:
        validation_result = self.validator.validate(new_list)
        if validation_result.errors :
            raise ValidationException()
        list = self.mapper.MapToList(new_list)
        result = self.repository.createList(list)
        response = self.mapper.MapToResponse(result)
        return response

    def update_list(self, updated_list: UpdateToDoListRequestDto) -> ToDoListResponseDto:
        validation_result = self.validator.validate(updated_list)
        if validation_result.errors :
            raise ValidationException()
        list = self.mapper.MapToList(updated_list)
        result = self.repository.updateList(list)
        response = self.mapper.MapToResponse(result)
        return response

    def change_list_state(self, updated_list: ChangeStateToDoListRequestDto) -> ToDoListResponseDto:
        validation_result = self.validator.validate(updated_list)
        if validation_result.errors :
            raise ValidationException()
        list = self.mapper.MapToList(updated_list)
        result = self.repository.UpdateList(list)
        response = self.mapper.MapToResponse(result)
        return response

    def create_task(self, new_task: CreateToDoTaskRequestDto) -> ToDoTaskResponseDto:
        validation_result = self.validator.validate(new_task)
        if validation_result.errors :
            raise ValidationException()
        task = self.mapper.MapToTask(new_task)
        result = self.repository.CreateTask(task)
        response = self.mapper.MapToResponse(result)
        return response

    def update_task(self, updated_task: UpdateToDoTaskRequestDto) -> ToDoTaskResponseDto:
        validation_result = self.validator.validate(updated_task)
        if validation_result.errors :
            raise ValidationException()
        task = self.mapper.MapToTask(updated_task)
        result = self.repository.UpdateTask(task)
        response = self.mapper.MapToResponse(result)
        return response

    def change_task_state(self, updated_task: ChangeStateToDoTaskRequestDto) -> ToDoTaskResponseDto:
        validation_result = self.validator.validate(updated_task)
        if validation_result.errors :
            raise ValidationException()
        task = self.mapper.MapToTask(updated_task)
        result = self.repository.UpdateTask(task)
        response = self.mapper.MapToResponse(result)
        return response
