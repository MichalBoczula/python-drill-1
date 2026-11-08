"""Guard the dependency direction of the four-layer architecture."""

import ast
from pathlib import Path

import pytest

SOURCE = Path(__file__).resolve().parents[2] / "src" / "todo_api"
FORBIDDEN = {
    "domain": (
        "todo_api.api",
        "todo_api.application",
        "todo_api.infrastructure",
        "fastapi",
        "pydantic",
        "pymongo",
    ),
    "application": (
        "todo_api.api",
        "todo_api.infrastructure",
        "fastapi",
        "pymongo",
    ),
    "infrastructure": ("todo_api.api",),
}


@pytest.mark.unit
def test_dependency_direction() -> None:
    for layer, modules in FORBIDDEN.items():
        for source in (SOURCE / layer).rglob("*.py"):
            tree = ast.parse(source.read_text(encoding="utf-8"))
            imports: list[str] = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    imports.append(node.module or "")

            for imported in imports:
                is_forbidden = any(
                    imported == forbidden or imported.startswith(forbidden + ".")
                    for forbidden in modules
                )
                assert not is_forbidden, (
                    f"{source.relative_to(SOURCE)} incorrectly imports {imported}"
                )
