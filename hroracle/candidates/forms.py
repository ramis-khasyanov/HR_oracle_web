import os
import psycopg2

from sqlalchemy import create_engine
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (StringField, BooleanField, DateField,
                     RadioField,SelectField,TextField, FloatField,
                     TextAreaField,SubmitField)

class CandidateForm(FlaskForm):

    list_sources = [
        ("e_source_hh",  "hh.ru"), 
        ("e_source_superjob",  "superjob.ru"),
        ("e_source_jobmo",  "job-mo.ru"), 
        ("e_source_ref",  "ref"), 
        ("e_source_other",  "other")
    ]
        
    list_positions = [
        ('e_position_reg','Сотрудник склада'),
        ('e_position_sen','Старший сотрудник склада'),
        ('e_position_lead','Ведущий сотрудник склада')
    ]
    
    list_entrance_type = [
        ('e_entrance_0','Отклик'),
        ('e_entrance_1','Поиск')
    ]
    
    engine = create_engine("postgresql://{user}:{password}@{host_ip}:{port}/{database}".format(user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], host_ip=os.environ['DB_HOST_IP'], port=os.environ['DB_PORT'], database="hroracledb"), echo=False, encoding='utf8')
    recruiter_query = engine.execute("SELECT e_recruiter FROM recruiters").fetchall()
    list_recruiters =[]
    for recruiter in recruiter_query:
        wtfid = "e_recruiter_" + recruiter[0].lower().replace(" ", "")
        name = recruiter[0]
        list_item = (wtfid, name)
        list_recruiters.append(list_item)

    
    e_name = StringField('Имя кандидата', validators=[DataRequired()])
    e_age = DateField('Возраст', validators=[DataRequired()])
    e_gender = RadioField('Пол:', choices=[('e_gender_male','Мужской'),('e_pos_female','Женский')], validators=[DataRequired()])
    e_commute = FloatField('Расстояние до работы', validators=[DataRequired()])
    e_recomended  = BooleanField("Есть рекомендаця", validators=[DataRequired()])
    e_position = RadioField('Должность', choices=list_positions, validators=[DataRequired()])
    e_days_to_hire = FloatField('Дней прошло после с первого контакта', validators=[DataRequired()])
    e_entrance_type = RadioField('Кто нашел', choices=list_entrance_type,validators=[DataRequired()])
    e_source = SelectField('Источник', choices = list_sources, validators=[DataRequired()])
    e_recruiter = SelectField('Рекрутер', choices = list_recruiters, validators=[DataRequired()])
    submit = SubmitField('Готово')