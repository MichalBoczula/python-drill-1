"""BDD acceptance exercises the real HTTP ASGI application."""

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from pytest_bdd import given, parsers, scenarios, then, when

from todo_api.api.main import create_app

pytestmark = pytest.mark.acceptance

scenarios("features/health.feature")


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(create_app()) as test_client:
        yield test_client


@given("a running API")
def running_api(client: TestClient) -> None:
    assert client is not None


@when(parsers.parse('I GET "{path}"'), target_fixture="response")
def get_resource(client: TestClient, path: str):
    return client.get(path)


@then(parsers.parse("the status is {status:d}"))
def response_status(response, status: int) -> None:
    assert response.status_code == status


@then("the body indicates liveness")
def liveness_body(response) -> None:
    assert response.json() == {"status": "alive"}


@then("the OpenAPI document includes the health routes")
def api_documentation(response) -> None:
    assert "/health/live" in response.json()["paths"]
    assert "/health/ready" in response.json()["paths"]
