# lesson2/app.py
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        message = request.form.get("message")
    return render_template("index.html", message=message)
