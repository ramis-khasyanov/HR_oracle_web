from hroracle import db
from datetime import datetime

class Candidate(db.Model):
    
    __tablename__ = "candidates"
    
    e_id = db.Column(db.Integer, primary_key=True)
    e_name = db.Column(db.String(255))
    e_age = db.Column(db.Integer)
    e_recomended  = db.Column(db.Integer)
    e_position = db.Column(db.String(255))
    e_recruiter = db.Column(db.String(255))
    e_days_to_hire = db.Column(db.Integer)
    e_commute = db.Column(db.Float)
    e_entrance_type = db.Column(db.Integer)
    e_source = db.Column(db.String(255))
    predictions = db.relationship("Candidate_predictions", "candidate", lazy=True)
    
    def __init__(self, e_name, e_age, e_recomended, e_position, e_recruiter, e_days_to_hire, e_commute, e_entrance_type, e_source):
        self.e_name = e_name
        self.e_age = e_age
        self.e_recomended = e_recomended
        self.e_position = e_position
        self.e_recruiter = e_recruiter
        self.e_days_to_hire = e_days_to_hire
        self.e_commute = e_commute
        self.e_entrance_type = e_entrance_type
        self.e_source = e_source
    
    def __repr__(self):
        return "Candidate {e_name}".format(e_name=self.e_name)
    
class Candidate_predictions(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    p_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    e_recruiter = db.Column(db.String(255))
    e_id = db.COlumn(db.Integer, db.ForeignKey("candidates.e_id"), nullable=False)
    e_age = db.Column(db.Integer)
    e_gender = db.Column(db.Integer)
    e_position_eng = db.Column(db.String(255))
    e_entrance_type = db.Column(db.Integer)
    e_source = db.Column(db.String(255))
    e_days_to_hire = db.Column(db.Integer)
    e_recomended = db.Column(db.Integer)
    e_salary_base = db.Column(db.Integer)
    e_commute = db.Column(db.Float)
    r_age = db.Column(db.Integer)
    r_tenure = db.Column(db.Integer)
    r_level = db.Column(db.Integer)
    u_department = db.Column(db.String(255))
    u_unit = db.Column(db.String(255))
    u_ntt = db.Column(db.Integer)
    u_tl_tenure = db.Column(db.Integer)
    u_tl_age = db.Column(db.Integer)
    u_tl_gender = db.Column(db.Integer)
    u_hires_week = db.Column(db.Integer)
    u_exits_week = db.Column(db.Integer)
    u_hires_month = db.Column(db.Integer)
    u_exits_month = db.Column(db.Integer)
    u_headcount = db.Column(db.Integer)
    u_age_mean = db.Column(db.Float)
    u_tenure_mean = db.Column(db.Float)
    u_gender_average = db.Column(db.Float)
    u_tl_active = db.Column(db.Integer)
    
