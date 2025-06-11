import argparse

from . import app


def main():
  parser = argparse.ArgumentParser(description="Run the Allidatar server")
  parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to run the server on")
  parser.add_argument("--port", type=int, default=5000, help="Port to run the server on")

  args = parser.parse_args()

  app.run(host=args.host, port=args.port)
