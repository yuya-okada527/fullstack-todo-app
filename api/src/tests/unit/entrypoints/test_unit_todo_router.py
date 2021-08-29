import pytest

from fastapi.testclient import TestClient

from tests.utils import TODO_API_PATH, make_url

@pytest.mark.parametrize("params", [
    [],
    ["start=0"],
    ["rows=0"],
    ["rows=100"]
])
def test_search_todo_200(client: TestClient, mocker, params):
    mocker.patch("service.todo_service.search_todo_service", return_value=[])
    assert client.get(make_url(TODO_API_PATH, params)).status_code == 200, f"params={params} must be valid params"

@pytest.mark.parametrize("params", [
    ["start=abc"],
    ["start=-1"],
    ["rows=abc"],
    ["rows=-1"],
    ["rows=101"]
])
def test_search_todo_422(client: TestClient, params):
    assert client.get(make_url(TODO_API_PATH, params)).status_code == 422, f"params={params} must be invalid params"
