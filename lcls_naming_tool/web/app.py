import sys
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from lcls_naming_tool import get_version, load_taxons, validate


sys.path.append(os.path.abspath('../'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

load_taxons()

@app.route('/', methods=('GET', 'POST'))
def index():

    version = get_version()

    if request.method == 'POST':
        lcls_name = str(request.form['lcls_name']).upper()

        flash(lcls_name, 'lcls_name')

        is_valid = validate(lcls_name)

        if is_valid:
            flash('Valid', 'valid')
        else:
            flash('Invalid', 'invalid')

    return render_template('index.html', version=version)
