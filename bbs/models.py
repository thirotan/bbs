"""models.py."""
# -*- coding: utf-8 -*-

from bbs import db


class Bbs(db.Model):
    __tablename__ = 'postmessage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    content = db.Column(db.Text)
