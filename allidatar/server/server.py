class Server:
  def __init__(self, host: str = "localhost", port: int = 8080):
    self.host = host
    self.port = port

  def start(self):
    print(f"Starting server on {self.host}:{self.port}")

  def stop(self):
    print("Stopping server.")


def main():
  import argparse

  parser = argparse.ArgumentParser(description="Start the Allidatar server.")
  parser.add_argument("--host", type=str, default="localhost", help="Host to run the server on")
  parser.add_argument("--port", type=int, default=8080, help="Port to run the server on")

  args = parser.parse_args()

  server = Server(host=args.host, port=args.port)
  server.start()

  try:
    # Keep the server running
    while True:
      pass
  except KeyboardInterrupt:
    print("", end="\r")
    server.stop()
