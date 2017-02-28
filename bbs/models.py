"""models.py."""
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import Integer, Text, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from bbs import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.Text)


class Thread(db.Model):
    __tablename__ = 'thread'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    thread_title = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text)
    message = db.Column(db.Text)
    ip_addr = db.Column(db.Text)
    user_agent = db.Column(db.Text)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'))
