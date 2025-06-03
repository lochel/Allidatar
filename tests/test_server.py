from allidatar import Server

def test_server():
  server = Server()
  server.start()
  server.stop()
  # If no exceptions are raised, the test passes
  assert True
