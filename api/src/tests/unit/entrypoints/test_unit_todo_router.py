import pytest
import json

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

@pytest.mark.parametrize("data", [
    {"name": "test", "status": "todo"},
    {"name": "test", "status": "doing"},
    {"name": "test", "status": "done"}
])
def test_create_todo_200(client: TestClient, mocker, data):
    mocker.patch("service.todo_service.create_todo_service", return_value=1)
    assert client.post(TODO_API_PATH, json.dumps(data)).status_code == 200, f"data={data} must be valid data"


@pytest.mark.parametrize("data", [
    {"name": "test"},
    {"status": "doing"},
    {"name": "test", "status": "hoge"}
])
def test_create_todo_200(client: TestClient, data):
    assert client.post(TODO_API_PATH, json.dumps(data)).status_code == 422, f"data={data} must be invalid data"