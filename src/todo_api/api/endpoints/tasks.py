"""Task endpoints will be written in the coding drills."""

from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Drill: start with POST /tasks, GET /tasks and GET /tasks/{task_id}.
