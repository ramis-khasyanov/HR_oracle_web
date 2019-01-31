from flask import render_template,url_for,flash, redirect,request,Blueprint
from hroracle import db
from hroracle.models import Candidate
from hroracle.candidates.forms import CandidateForm

candidates = Blueprint('candidates',__name__)

@candidates.route('/new_candidate', methods=['GET', 'POST'])
def new_candidate():
    form = CandidateForm()
    
    if form.validate_on_submit():
        candidate = Candidate(
                e_name = form.e_name.data,
                e_position_eng = form.e_position_eng.data,
                e_salary_base = form.e_salary_base.data,
                e_age = form.e_age.data,
                e_gender = form.e_gender.data,
                e_entrance_type = form.e_entrance_type.data,
                e_source = form.e_source.data,
                e_days_to_hire = form.e_days_to_hire.data,
                e_recomended = form.e_recomended.data,
                e_commute = form.e_commute.data,
                e_recruiter = form.e_recruiter.data
            )
        db.session.add(candidate)
        db.session.commit()
        flash("Кандидат добавлен")
        return redirect(url_for('core.index'))
    return render_template('new_candidate.html', form=form)