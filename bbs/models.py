"""models.py."""
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import Integer, Text, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from bbs import db


class Thread(db.Model):
    __tablename__ = 'thread'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    thread_name = db.Column(db.Text)
    # titles = db.relationship('Title', backref='thread', lazy='dynamic')


class Title(db.Model):
    __tablename__ = 'title'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    thread_id = db.Column(db.Integer, db.ForeignKey('thireads.id'))
    # messages = db.relationship('Message', backref='title', lazy='dynamic')


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    message = db.Column(db.Text)
    ip_addr = db.Column(db.Text)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    board_id = db.Column(db.Integer, db.ForeignKey('titles.id'))
