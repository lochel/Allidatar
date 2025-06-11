import subprocess
import time

import pytest
import requests


@pytest.fixture(scope="module", autouse=True)
def module_setup_teardown():
  server_process = subprocess.Popen(["allidatar-server"], cwd="tests/server")
  time.sleep(1)  # wait for the server to start

  yield

  server_process.terminate()

def test_404():
  response = requests.get("http://127.0.0.1:5000/api/404")
  assert response.status_code == 404


def test_api_time():
  response = requests.get("http://127.0.0.1:5000/api/time")
  assert response.status_code == 200
  assert 'time' in response.json()
