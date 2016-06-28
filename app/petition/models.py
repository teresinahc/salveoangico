#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


class Signature(Base):

    __tablename__ = 'signatures'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    registration = db.Column(db.String(14), nullable=False, unique=True)

    def __init__(self, name, email, registration):

        self.name = name
        self.email = email
        self.registration = registration

    def __repr__(self):
        return '<Signature %r>' % (self.name)
