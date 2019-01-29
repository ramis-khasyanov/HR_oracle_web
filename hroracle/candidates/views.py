from flask import render_template,url_for,flash, redirect,request,Blueprint
from hroracle import db
from hroracle.models import Candidate
from hroracle.candidates.forms import CandidateForm

candidates = Blueprint('candidates',__name__)

@candidates.route('/new_candidate', methods=['GET', 'POST'])
def new_candidate():
    form = CandidateForm()
    return render_template('new_candidate.html', form=form)