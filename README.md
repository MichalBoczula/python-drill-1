# Python Drill 1 — FastAPI + MongoDB

Hands-on Python interview practice. The goal is to learn Python by implementing
To-Do operations yourself, in a familiar four-layer Clean Architecture structure.

## Architecture

| Layer | Responsibility |
| --- | --- |
| `src/todo_api/api` | FastAPI routes, validation errors, composition and DI |
| `src/todo_api/application` | Use-case services, request and response schemas |
| `src/todo_api/domain` | Pure-Python entities and repository ports |
| `src/todo_api/infrastructure` | Async PyMongo, repositories, mapping, settings |

Domain must not import FastAPI, Pydantic or MongoDB. A unit architecture test
checks the dependency direction.

## Prerequisites

- [uv](https://docs.astral.sh/uv/) and Docker (for MongoDB/integration tests).
- Python 3.14 is selected by `.python-version`; uv can install it.

## Quick start

```bash
uv python install 3.14
uv sync
docker compose up -d mongodb
uv run uvicorn todo_api.api.main:app --reload
```

Open <http://localhost:8000/docs>. Check:
- `GET /health/live` — process is alive (independent of Mongo).
- `GET /health/ready` — MongoDB responds to `ping`.
- `GET /openapi.json` — generated API contract.

You can alternatively start both services with `docker compose up -d --build`.
Copy `.env.example` to `.env` if you want to override defaults.
Never commit real credentials.

## Quality and test layers

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest -m unit
uv run pytest -m integration       # Requires Docker for Testcontainers
uv run pytest -m acceptance
uv run pytest                      # All categories
```

- **Unit:** isolated domain, request validation, mapping and architecture checks.
- **Integration:** a real disposable MongoDB using Testcontainers.
- **Acceptance:** Gherkin scenarios through HTTPX/Starlette TestClient.

GitHub Actions runs Ruff and all three groups. As a first contribution,
run `uv lock` locally and commit the generated `uv.lock` so all future
environments resolve the exact same dependency graph.

## Drill: implement To-Do CRUD yourself

The application service, repository port, MongoDB adapter and task router are
**intentionally unfinished**. They are placeholders for coding practice.

1. Add `POST /tasks` and implement `TaskService.create`.
2. Implement `MongoTaskRepository.add` and map the document.
3. Add `GET /tasks` and `GET /tasks/{task_id}`.
4. Implement updating and deleting tasks, with validation and 404 handling.
5. Write unit, real MongoDB integration and Gherkin acceptance tests.

Do not solve the drills by copying generated code: type the solution yourself.

## Python/C# conceptual mapping

- `Protocol` ≈ a small C# interface for dependency inversion.
- `dataclass` ≈ a lightweight entity/value container.
- Pydantic `BaseModel` ≈ request/response contract with runtime validation.
- FastAPI `Depends` ≈ scoped composition/dependency injection (different lifecycle semantics).
- PyMongo `AsyncMongoClient` ≈ asynchronous MongoDB driver.

This is a learning application, not a production-grade deployed service.
