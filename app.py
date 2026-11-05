"""Intentionally vulnerable, non-production application for Wingmate scan verification."""

from flask import Flask, jsonify, request
from lookup import find_customer

app = Flask(__name__)


@app.get("/customers")
def customers():
    return jsonify(find_customer(request.args.get("name", "")))
