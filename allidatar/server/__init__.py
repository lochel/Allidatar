import json
import secrets
from sys import stderr

try:
  with open('data/config.json') as f:
    config = json.load(f)
except FileNotFoundError:
  print('\033[91mWarning: Could not find or load data/config.json\033[0m', file=stderr)
  config = {'SECRET_KEY': secrets.token_hex(16)}

import flask_login
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = config['SECRET_KEY']

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

from . import routes
from .server import main
