from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.notes.forms import EmptyForm, NoteForm
from app.models import User, Note
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    notes = Note.query.all()
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(body=form.note.data, author=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Note saved.')
        return redirect('/notes')
    printThis = 'string'
    return render_template('notes.html', title=('Home'), notes = notes, form = form)
