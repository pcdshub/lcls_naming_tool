import os
import sys

from flask import Flask, flash, redirect, render_template, request, url_for

from lcls_naming_tool import get_version, load_taxons, validate

sys.path.append(os.path.abspath("../"))

app = Flask(__name__)

SECRET_KEY = os.urandom(24)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/", methods=("GET", "POST"))
def index():
    load_taxons()

    version = get_version()

    if request.method == "POST":
        lcls_name = str(request.form["lcls_name"]).upper()

        flash(lcls_name, "lcls_name")

        is_valid = validate(lcls_name)

        if is_valid:
            flash("Valid", "valid")
        else:
            flash("Invalid", "invalid")

    return render_template("index.html", version=version)
