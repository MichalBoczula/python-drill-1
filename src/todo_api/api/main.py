"""FastAPI bootstrap and composition root."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from todo_api.api.endpoints import health, tasks
from todo_api.api.exception_handlers import register_exception_handlers
from todo_api.infrastructure.config import get_settings
from todo_api.infrastructure.database.mongodb import create_client, get_database


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings = get_settings()
    client = create_client(settings)
    app.state.mongo_client = client
    app.state.database = get_database(client, settings)
    try:
        yield
    finally:
        await client.close()


def create_app() -> FastAPI:
    app = FastAPI(title=get_settings().app_name, lifespan=lifespan)
    register_exception_handlers(app)
    app.include_router(health.router)
    app.include_router(tasks.router)
    return app


app = create_app()
