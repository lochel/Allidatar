from datetime import datetime

from flask import jsonify

from . import app


@app.route('/api/time')
def api_time():
  return jsonify({"time": datetime.utcnow().isoformat() + 'Z'})

@app.errorhandler(404)
def page_not_found(e):
  response = {'error': 404}
  return jsonify(response), 404
