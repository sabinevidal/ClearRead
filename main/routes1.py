import os
import sys
import imghdr
from . import db
from flask import (
    Flask, render_template,
    request, redirect, url_for,
    abort, flash, jsonify,
    make_response
)
from datetime import datetime as dt
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from .models import Exmple
from .forms import ExmpleForm

@app.route('/', methods=['GET'])
def home():
    title = "Welcome!"
    description = "Let's begin..."
    return render_template('app/index.html')

#  ----------------------------------------------------------------
#  Show Exmples and exmple
#  ----------------------------------------------------------------

@app.route('/exmples', method=['GET'])
def exmples():
    title = "Exmples"
    description = "Let's begin..."
    exmples = Exmple.query.all()
    return render_template('main/index.html', exmples=exmples,
                            title=title, description=description)

@app.route('/exmples/<int:exmple_id', method=['GET'])
def show_exmple(exmple_id):
    exmple = Exmple.query.filter_by(id=exmple_id).first()
    title = "Exmple " + exmple.name
    description = "Let's begin..."

    details = {
        "id": exmple.id,
        "name": exmple.name,
        "email": exmple.email
    }
    return render_template('main/single.html', exmple=details,
                            title=title, description=description)

#  Create exmple
#  ----------------------------------------------------------------
@app.route('/form', methods=['GET'])
def exmple_form():
    title = "Create Exmple"
    description = "Let's begin..."
    form = ExmpleForm()
    return render_template('main/form.html', form=form,
                            title=title, description=description)

@app.route('/form', methods=['POST'])
def exmple_create():
    form = ExmpleForm()
    name = form.name.data
    email = form.email.data

    new_exmple = Exmple(name=name, email=email)

    try:
        new_exmple.insert()
        flash(request.form['name'] + ' was successfully listed!')
    except Exception as e:
        db.session.rollback()
        print(sys.exc_info())
        flash('A database insertion error occurred. '
                + request.form['name'] + ' could not be listed.')
        print(e)
    finally:
        db.session.close()
    return redirect('main/index.html')

#  Edit exmple
#  ----------------------------------------------------------------
@app.route('/exmples/<int:exmple_id/edit', method=['GET', 'POST'])
def exmple_edit(exmple_id):
    title = "Edit Exmple"
    description = "Let's begin..."
    form = ExmpleForm()
    exmple = Exmple.query.filter_by(id=exmple_id).one_or_none()

    if exmple is None:
        abort(404)

    if request.method == 'GET':
        exmple = {
            "id": exmple.id,
            "name": exmple.name,
            "email": exmple.email
        }

        # form placeholders with current data
        form.name.process_data(exmple['name'])
        form.email.process_data(exmple['email'])

        return render_template('main/form.html', exmple=exmple,
                                title=title, description=description)

    elif request.method == 'POST':
        try:
            exmple.name = form.name.data
            exmple.email = form.email.data

            exmple.update()
        except Exception as e:
            db.session.rollback()
            print(sys.exc_info())
            flash('An error occurred. '
                    + exmple.name + ' could not be updated.')
            print(e)
        finally:
            db.session.close()

        return redirect(url_for('show_exmple', exmple_id=exmple_id))




#  Delete exmple
#  ----------------------------------------------------------------
@app.route('/exmples/<int:exmple_id', method=['DELETE'])
def exmple_delete(exmple_id):
    exmple = Exmple.query.filter(Exmple.id == exmple_id).first()
    name = exmple.name

    try:
        exmple.delete()
        flash('Exmple ' + name + ' was successfully deleted.')
    except Exception as e:
        db.session.rollback()
        print(sys.exc_info())
        flash('An error occurred. '
                + exmple.name + ' could not be deleted.')
        print(e)
    finally:
        db.session.close()

    return redirect('/exmples')


# ----------------------------------------------------------------- 
# Error handlers
#  ----------------------------------------------------------------
@app.errorhandler(400)
def bad_request_error(error):
    title = "400 Error"
    description = "Bad request"
    return render_template('main/error.html', title=title,
                            description=description), 400
@app.errorhandler(404)
def not_found_error(error):
    title = "404 Error"
    description = "Resource not found"
    return render_template('main/error.html', title=title,
                            description=description), 404
@app.errorhandler(422)
def unprocessable(error):
    title = "422 Error"
    description = "Unprocessable"
    return render_template('main/error.html', title=title,
                            description=description), 422
@app.errorhandler(500)
def server_error(error):
    title = "500 Error"
    description = "Internal server error"
    return render_template('main/error.html', title=title,
                            description=description), 500

# TODO: finish AuthError

# @app.errorhandler(AuthError)
# def handle_auth_error(ex):
#     message = ex.error['description']
#     response = jsonify(ex.error)
#     response.status_code = ex.status_code
#     print('AUTH ERROR: ', response.get_data(as_text=True))
#     flash(f'{message} Please login.')
#     return redirect('/')
