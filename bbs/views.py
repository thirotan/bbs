"""views.py."""
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Thread, Title, Message

app = Blueprint('app', __name__)


@app.route('/')
def index():
    """index page."""
    data = Bbs.query.order_by(Bbs.id.desc()).all()
    return render_template('index.html', contents=data)


@app.route('/post_message', methods=['POST'])
def post_message():
    post_name = request.form['name']
    post_content = request.form['content']
    save_data = Message(
        name=post_name,
        message=post_content
        ip_addr = '127.0.0.1'
    )
    db.session.add(save_data)
    db.session.commit()

    return redirect(url_for('app.index'))
