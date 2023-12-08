"""
Trying to implement Getify's Periodic Table Speller exercise
https://frontendmasters.com/courses/algorithms-practice/periodic-table-speller-setup/
but with Python/Flask/HTMX.
"""
from flask import Flask, request, render_template

from speller import check
from template import extend_filters


app = Flask(__name__, template_folder="html")
app.secret_key = b"Beryllium"
extend_filters(app)


@app.route("/")
def index():
    return render_template("template.html", res=" ")


@app.route("/spell", methods=["POST"])
def spell():
    res = check(request.form["enterWord"])
    # print(f"result of check: {res}")
    return render_template("spelled_word.html", res=res)


if __name__ == "__main__":
    app.run(port=5001)
