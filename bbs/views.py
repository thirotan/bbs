"""views.py."""
# -*- coding: utf-8 -*-

from flask import Blueprint, Flask, redirect, render_template, request, url_for
from .models import Bbs

app = Blueprint('app', __name__)


@app.route('/')
def index():
    """index page."""
    return render_template('index.html')


@app.route('/post_message', methods=['POST'])
def post_message():
    name = request.form['name']
    content = request.form['content']
    return redirect(url_for('index'))
