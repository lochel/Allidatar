import subprocess
import time

import requests


def test_404():
  server_process = subprocess.Popen(["allidatar-server"])
  time.sleep(1)  # wait for the server to start

  try:
    response = requests.get("http://127.0.0.1:5000/api/404")
    assert response.status_code == 404
  finally:
    server_process.terminate()


def test_api_time():
  server_process = subprocess.Popen(["allidatar-server"])
  time.sleep(1)  # wait for the server to start

  try:
    response = requests.get("http://127.0.0.1:5000/api/time")
    assert response.status_code == 200
    assert 'time' in response.json()
  finally:
    server_process.terminate()
