FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app
ENV UV_NO_DEV=1
ENV PATH="/app/.venv/bin:$PATH"
COPY pyproject.toml README.md ./
COPY src ./src
RUN uv sync --no-dev --no-editable

EXPOSE 8000
CMD ["uvicorn", "todo_api.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
