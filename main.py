"""
TODO
trying to implement this
https://frontendmasters.com/courses/algorithms-practice/periodic-table-speller-setup/
but with Python/Flask/HTMX
"""
from flask import Flask, request, render_template

from speller import check


app = Flask(__name__, template_folder="html")

app.secret_key = b"Beryllium"


@app.route("/")
def index():
    return render_template("template.html")


@app.route("/spell", methods=["POST"])
def spell():
    print(f"Transmitted value: {request.form['enterWord']}")
    res = check(request.form["enterWord"])
    print(f"result of check: {res}")
    return "Could not spell it!"


if __name__ == "__main__":
    app.run(port=5001)
