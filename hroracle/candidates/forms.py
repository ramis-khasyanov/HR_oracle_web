import os
import psycopg2

from sqlalchemy import create_engine
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (StringField, BooleanField, DateField,
                     RadioField,SelectField,TextField, FloatField,
                     TextAreaField,SubmitField)
from hroracle.models import Recruiter


class CandidateForm(FlaskForm):
    
    list_gender = [
        ("0", "Мужской"),
        ("1", "Женский")
        ]
    
    list_sources = [
        ("headhunter",  "hh.ru"), 
        ("superjob",  "superjob.ru"),
        ("jobmo",  "Job-MO.ru"), 
        ("rabota", "rabota.ru"),
        ("zarplata", "zarplat.ru"),
        ("ref",  "Рекомендация"), 
        ("lamoda", "Сайт Lamoda"),
        ("other",  "Другое")
    ]
        
    list_positions = [
        ('DC_employee','Сотрудник склада'),
        ('Senior_DC_employee','Старший сотрудник склада'),
        ('Leading_DC_employee','Ведущий сотрудник склада')
    ]
    
    list_entrance_type = [
        ("0",'Отклик'),
        ("1",'Поиск')
    ]
    
    list_recruiters = []
    recruiters_query = Recruiter.query.all()
    for item in recruiters_query:
        list_recruiters.append((item.e_recruiter, item.e_recruiter))
    
    

    
    '''
    engine = create_engine("postgresql://{user}:{password}@{host_ip}:{port}/{database}".format(user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'], host_ip=os.environ['DB_HOST_IP'], port=os.environ['DB_PORT'], database="hroracledb"), echo=False, encoding='utf8')
    recruiter_query = engine.execute("SELECT e_recruiter FROM recruiters").fetchall()
    list_recruiters =[]
    for recruiter in recruiter_query:
        wtfid = "e_recruiter_" + recruiter[0].lower().replace(" ", "")
        name = recruiter[0]
        list_item = (wtfid, name)
        list_recruiters.append(list_item)
    '''
    
    e_name = StringField('Имя кандидата', validators=[DataRequired()])
    e_age = StringField('Возраст')
    e_gender = RadioField('Пол:', choices=list_gender)
    e_commute = StringField('Расстояние до РЦ (км)')
    e_recomended  = BooleanField("Есть рекомендация")
    e_position_eng = SelectField('Должность', choices=list_positions)
    e_days_to_hire = StringField('Дней прошло с первого контакта')
    e_entrance_type = RadioField('Как к нам пришел', choices=list_entrance_type)
    e_source = SelectField('Источник', choices=list_sources)
    e_recruiter = SelectField('Рекрутер',  choices=list_recruiters)
    submit = SubmitField('Готово')