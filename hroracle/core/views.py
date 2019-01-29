from flask import request, Blueprint, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField,
                     RadioField,SelectField,TextField, FloatField,
                     TextAreaField,SubmitField)
                     
import os
import psycopg2
from sqlalchemy import create_engine
from wtforms.validators import DataRequired

core = Blueprint("core",__name__)


@core.route('/')
def index():
    return render_template('index.html')
    
@core.route('/info')
def info():
    return render_template('info.html')