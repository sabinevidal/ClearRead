import sys
from main.__init__ import db
from flask import (
    Flask, render_template,
    request, redirect, url_for,
    abort, flash, jsonify,
    make_response,
    Blueprint
)
from datetime import datetime as dt
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy

from main.models import Exmple
from main.forms import ExmpleForm

# Blueprint Configuration
exmple_bp = Blueprint(
    'exmple_bp', __name__,
    template_folder='templates'
)

#  ----------------------------------------------------------------
#  Show Exmples and exmple

@exmple_bp.route('/exmples', methods=['GET'])
def exmples():
    title = "Exmples"
    description = "Let's begin..."
    exmples = Exmple.query.all()
    return render_template('index.html', exmples=exmples,
                            title=title, description=description)

@exmple_bp.route('/exmples/<int:exmple_id>', methods=['GET'])
def show_exmple(exmple_id):
    exmple = Exmple.query.filter_by(id=exmple_id).first()
    title = "Exmple " + exmple.name
    description = "Let's begin..."

    details = {
        "id": exmple.id,
        "name": exmple.name,
        "email": exmple.email
    }
    return render_template('single.html', exmple=details,
                            title=title, description=description)

#  ----------------------------------------------------------------
#  Create exmple

@exmple_bp.route('/exmples/form', methods=['GET'])
def exmple_form():
    title = "Create Exmple"
    form_heading = "Enter Information"
    form = ExmpleForm()
    return render_template('form.html', form=form,
                            title=title, form_heading=form_heading)

@exmple_bp.route('/exmples/form', methods=['POST'])
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
    return redirect(url_for('exmple_bp.exmples'))

#  ----------------------------------------------------------------
#  Edit exmple

@exmple_bp.route('/exmples/<int:exmple_id>/edit', methods=['GET', 'POST'])
def exmple_edit(exmple_id):
    title = "Edit Exmple"
    form_heading = "Edit information"
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

        return render_template('form.html', form=form, exmple=exmple,
                                title=title, form_heading=form_heading)

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

        return redirect(url_for('exmple_bp.exmples'))

#  ----------------------------------------------------------------
#  Delete exmple

@exmple_bp.route('/exmples/<int:exmple_id>/delete', methods=['GET'])
def exmple_delete(exmple_id):
    exmple = Exmple.query.filter(Exmple.id == exmple_id).first_or_none()
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

    return redirect(url_for('exmple_bp.exmples'))

