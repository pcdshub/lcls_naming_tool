from flask import Flask, render_template, request, url_for, flash, redirect
from lcls_naming_tool import load_taxons, validate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        pv_name = str(request.form['pv_name']).upper()

        flash(pv_name, 'pv_name')

        load_taxons()

        is_valid = validate(pv_name)

        if is_valid:
            flash('Valid', 'valid')
        else:
            flash('Invalid', 'invalid')
            return redirect(url_for('index'))

    return render_template('index.html')