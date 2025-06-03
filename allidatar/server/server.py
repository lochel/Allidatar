class Server:
  def __init__(self, host: str = "localhost", port: int = 8080):
    self.host = host
    self.port = port

  def start(self):
    print(f"Starting server on {self.host}:{self.port}")

  def stop(self):
    print("Stopping server.")
