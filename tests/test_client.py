from allidatar import Client

def test_client():
  client = Client()
  client.start()
  client.stop()
  # If no exceptions are raised, the test passes
  assert True
