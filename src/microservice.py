import logging
from os import getenv
import http.client as http_client

from flask import Flask, render_template

JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')
http_client.HTTPConnection.debuglevel = 1

app = Flask(__name__)
app.secret_key = b'7a58153c1d2a0d5b8f3a8fc343a18c7ced4a4c4e11085ce0664bb72cd96fc3ed88d3b9dbdcb32063'


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello(name=None):
    return render_template('index.jinja2', name=name)


@app.route('/health/')
def health():
    return "ok"


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='9080', debug=True)
