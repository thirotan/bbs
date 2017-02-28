"""views.py."""
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Thread, Category, Message

app = Blueprint('app', __name__)


@app.route('/')
def index():
    """index page."""
    data = Message.query.order_by(Message.id.desc()).all()
    return render_template('index.html', contents=data)


@app.route('/post_message', methods=['POST'])
def post_message():
    post_name = request.form['username']
    post_content = request.form['message']
    save_data = Message(
        username=post_name,
        message=post_content,
        ip_addr = '127.0.0.1',
        user_agent = 'UA12345',
        thread_id = 1
    )
    db.session.add(save_data)
    db.session.commit()

    return redirect(url_for('app.index'))
