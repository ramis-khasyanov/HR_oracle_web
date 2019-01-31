from flask import render_template,url_for,flash, redirect,request,Blueprint
from hroracle import db
from hroracle.models import Candidate, Candidate_predictions
from hroracle.candidates.forms import CandidateForm
import requests
import json

candidates = Blueprint('candidates',__name__)

@candidates.route('/new_candidate', methods=['GET', 'POST'])
def new_candidate():
    form = CandidateForm()
    
    if form.validate_on_submit():
        candidate_features = {
            "e_id": db.session.query(Candidate).count() + 1,
            "e_name": form.e_name.data,
            "e_position_eng": form.e_position_eng.data,
            "e_salary_base": form.e_salary_base.data,
            "e_age": form.e_age.data,
            "e_gender": form.e_gender.data,
            "e_entrance_type": form.e_entrance_type.data,
            "e_source": form.e_source.data,
            "e_days_to_hire": form.e_days_to_hire.data,
            "e_recomended": form.e_recomended.data,
            "e_commute": form.e_commute.data,
            "e_recruiter": form.e_recruiter.data
        }
        
        candidate = Candidate(
                e_id = candidate_features["e_id"],
                e_name = candidate_features["e_name"],
                e_position_eng = candidate_features["e_position_eng"],
                e_salary_base = candidate_features["e_salary_base"],
                e_age = candidate_features["e_age"],
                e_gender = candidate_features["e_gender"],
                e_entrance_type = candidate_features["e_entrance_type"],
                e_source = candidate_features["e_source"],
                e_days_to_hire = candidate_features["e_days_to_hire"],
                e_recomended = candidate_features["e_recomended"],
                e_commute = candidate_features["e_commute"],
                e_recruiter = candidate_features["e_recruiter"]
            )
        
        db.session.add(candidate)
        db.session.commit()
        json_obj = json.dumps(candidate_features)
        #response = requests.post('https://hroraclemachine.herokuapp.com/predict', json=json_obj)
        return redirect(url_for('candidates.candidate_prediction', e_id=candidate.e_id))
    return render_template('new_candidate.html', form=form)
    
   
@candidates.route('/<int:e_id>')
def candidate_prediction(e_id):
    #candidate_prediction = Candidate_predictions.query.get_or_404(e_id)
    candidate = Candidate.query.get(e_id)
    return render_template('candidate_predictions.html', candidate=candidate)
