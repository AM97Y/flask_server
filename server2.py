from flask import Flask, jsonify, request
import requests

import numpy as np

app = Flask(__name__)


@app.route('/detect/')
def sample():
    print('ELEM', request.args.to_dict())
    return jsonify({
        "img": ["hello", "world"],

    })


if __name__ == '__main__':
    app.run(debug=True)
