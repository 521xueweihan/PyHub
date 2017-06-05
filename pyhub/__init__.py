import logging
from logging.handlers import RotatingFileHandler
import traceback

from flask import Flask, request


app = Flask(__name__)


@app.after_request
def after_request(response):
    logger.info('%s %s %s %s %s', request.remote_addr, request.method,
                request.scheme, request.full_path, response.status)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
        request.remote_addr, request.method,
        request.scheme, request.full_path, tb)
    return e.status_code

handler = RotatingFileHandler('%s.log' % app.name, maxBytes=100000, backupCount=3)
logger = logging.getLogger(app.name)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

from pyhub.views import index, manage