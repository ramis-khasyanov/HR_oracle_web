from flask import render_template,url_for,flash, redirect,request,Blueprint
from hroracle import db
from hroracle.models import Candidate
from hroracle.candidates.forms import CandidateForm