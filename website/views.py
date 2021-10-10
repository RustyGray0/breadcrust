from flask import Blueprint, render_template, request, redirect, flash, send_file
from flask.helpers import url_for
from flask_login import login_required, current_user
from .models import FileContents
from . import db
from io import BytesIO

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    if request.method == 'POST':
        pass

    return render_template("home.html", user=current_user)

@views.route('/fileinput')
def file_input():
    return render_template("fileInput.html", user=current_user)

@views.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']

    newFile = FileContents(name=file.filename, data=file.read(), user_id=current_user.id)
    db.session.add(newFile)
    db.session.commit()

    flash(f'Added {file.filename} to database')
    return redirect(url_for('views.file_input'))