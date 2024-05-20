from flask import Flask
from flask import request

import sys

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    print(request.get_json(), file=sys.stderr)
    return "ok"

