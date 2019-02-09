from flask import request, Blueprint, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField,
                     RadioField,SelectField,TextField, FloatField,
                     TextAreaField,SubmitField)
                     
from hroracle.models import Candidate

core = Blueprint("core",__name__)


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    candidates = Candidate.query.order_by(Candidate.e_date_entered.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', candidates=candidates)

    
@core.route('/info')
def info():
    return render_template('info.html')
