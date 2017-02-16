"""views.py."""
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Bbs

app = Blueprint('app', __name__)


@app.route('/')
def index():
    """index page."""
    data = Bbs.query.all()
    return render_template('index.html', contents=data)


@app.route('/post_message', methods=['POST'])
def post_message():
    post_name = request.form['name']
    post_content = request.form['content']
    save_data = Bbs(
        name=post_name,
        content=post_content
    )
    db.session.add(save_data)
    db.session.commit()

    data = Bbs.query.all()
    return redirect(url_for('app.index'))
