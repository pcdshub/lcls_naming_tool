import sys
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from lcls_naming_tool import get_version, load_taxons, validate


sys.path.append(os.path.abspath('../'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/', methods=('GET', 'POST'))
def index():

    version = get_version()

    if request.method == 'POST':
        pv_name = str(request.form['pv_name']).upper()

        flash(pv_name, 'pv_name')

        load_taxons()

        is_valid = validate(pv_name)

        if is_valid:
            flash('Valid', 'valid')
        else:
            flash('Invalid', 'invalid')

    return render_template('./index.html', version=version)
