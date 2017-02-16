"""views.py."""
# -*- coding: utf-8 -*-

from flask import Blueprint, Flask, redirect, render_template, request, url_for

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
    name = request.form['name']
    content = request.form['content']
    data = Bbs.query.all()
    return render_template('index.html', contents=data)
