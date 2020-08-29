from flask import Flask, render_template, redirect
import json

app = Flask(__name__)


@app.route("/")
def hw():
    return "Hello, backend!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
