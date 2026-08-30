from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from app.send_page import send_page

app = Flask(__name__)
csrf = CSRFProtect(app)


@app.route("/", methods=["GET"])
def index():
    """Returns index template."""
    return render_template("index.html", status="")


@app.route("/", methods=["POST"])
def send():
    """POST function"""
    result = send_page(
        name=request.form.get("name"),
        email=request.form.get("email"),
        message=request.form.get("message"),
    )
    status = "success" if result[0] else "fail"
    return render_template("index.html", status=status)
