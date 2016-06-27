#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from config import RESULTS_PER_PAGE
from app import db
from app.petition.forms import SignatureForm
from app.petition.models import Signature
from sqlalchemy import func

mod_petition = Blueprint('petitions', __name__)

@mod_petition.route('/', methods=['GET', 'POST'])
@mod_petition.route('/<int:page>', methods=['GET', 'POST'])
def create(page=1):

    form = SignatureForm(request.form)
    signatures_count = Signature.query.count()
    signatures = Signature.query.order_by('date_created DESC').paginate(page, RESULTS_PER_PAGE, False)

    if form.validate_on_submit():
        signature = Signature(
            name=form.name.data,
            email=form.email.data,
            registration=form.registration.data
        )

        if signature:
            db.session.add(signature)
            db.session.commit()

            flash('Assinatura realizada com sucesso!',
                  'success-message')

            return redirect('/#sign-form')

        flash('Ocorreu um erro ao tentar salvar sua assinatura',
              'error-message')

    return render_template(
        'petition/new.html',
        form=form,
        signatures_count=signatures_count,
        signatures=signatures
    )
