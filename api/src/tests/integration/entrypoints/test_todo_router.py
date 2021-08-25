import pytest
from fastapi.testclient import TestClient
from main import app
from tests.utils import make_url

client = TestClient(app)

TODO_API_PATH = "/v1/todos"


@pytest.mark.parametrize("params", [
    []
])
def test_get_todo(params):
    url = make_url(TODO_API_PATH, params)
    response = client.get(url)
    assert response.status_code == 200, f"params={params} test failed.  url={url}"
