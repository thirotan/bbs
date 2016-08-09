"""views.py."""
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from .models import Bbs

app = Blueprint('app', __name__)


@app.route('/')
def index():
    """index page."""
    return render_template('index.html')
