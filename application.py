import json
import logging.config

from flask import Flask, render_template, request

from config import get_logger
from helper import get_activity


app = Flask(__name__)
LOGGING = get_logger()
logging.config.dictConfig(LOGGING)
logging.captureWarnings(True)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    activity_type = request.form.get('type')
    response = get_activity(activity_type=activity_type)
    response_json =  response.json()
    status_code = response.status_code 

    return render_template('index.html', response=response_json), response.status_code
