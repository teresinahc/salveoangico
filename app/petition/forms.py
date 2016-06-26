#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, ValidationError
from wtforms.validators import Required, Email
from pycpfcnpj import cpfcnpj
from app import db
from models import Signature
from utils.unique import Unique

def validate_registration(form, field):
    # TODO: Improve string sanatization
    value = field.data.replace('.', '')
    value = value.replace('-', '')

    if not cpfcnpj.validate(value):
        raise ValidationError("O CPF não é válido.")


class SignatureForm(Form):
    name = TextField(
        'Nome completo',
        [Required(message='Preencha com seu nome completo')]
    )
    email = TextField(
        'Endereço de email',
        [Email(), Required(message='Preencha com seu endereço de email'), Unique(Signature, Signature.email)]
    )
    registration = TextField(
        'CPF',
        [Required(message='Preencha com seu CPF'), validate_registration, Unique(Signature, Signature.registration)]
    )
