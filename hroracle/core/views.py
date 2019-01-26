from flask import request, Blueprint, Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)

core = Blueprint("core",__name__)



class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    e_name = StringField('Employee name')
    e_recomended  = BooleanField("Have Recomendation within company?")
    e_position = RadioField('Position:', choices=[('pos_reg','Regular'),('pos_sen','Senior'),('pos_lead','Leading')])
    e_commute = TextAreaField()
    submit = SubmitField('Submit')

@core.route('/')
def index():
    return render_template("index.html")
    
@core.route('/form', methods=['GET', 'POST'])
def form():
    form = InfoForm()

    session['e_name'] = form.e_name.data
    session['e_recomended'] = form.e_recomended.data
    session['e_position'] = form.e_position.data
    session['e_commute'] = form.e_commute.data
    
    return render_template('form.html', form=form)