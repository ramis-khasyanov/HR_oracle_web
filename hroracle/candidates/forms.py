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

    
    e_name = StringField('Имя кандидата', validators=[DataRequired()], default="Хасянов Рамис Равилевич")
    e_age = StringField('Возраст', validators=[DataRequired()], default=28)
    e_gender = StringField('Пол:', validators=[DataRequired()], default=0)
    e_commute = StringField('Расстояние до работы', validators=[DataRequired()], default=65)
    e_recomended  = StringField("Есть рекомендаця", validators=[DataRequired()], default=1)
    e_position_eng = StringField('Должность', validators=[DataRequired()], default="DC employee")
    e_salary_base = StringField("Фиксированный оклад", validators=[DataRequired()], default=10500)
    e_days_to_hire = StringField('Дней прошло после с первого контакта', validators=[DataRequired()], default=35)
    e_entrance_type = StringField('Кто нашел', validators=[DataRequired()], default=1)
    e_source = StringField('Источник', validators=[DataRequired()], default="headhunter")
    e_recruiter = StringField('Рекрутер', validators=[DataRequired()], default="Yuliya Almazova")
    submit = SubmitField('Готово')