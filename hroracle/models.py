from hroracle import db
from datetime import datetime

class Candidate(db.Model):
    
    __tablename__ = "candidates"
    
    e_id = db.Column(db.Integer, primary_key=True)
    e_name = db.Column(db.String(255))
    e_age = db.Column(db.Integer)
    e_gender = db.Column(db.Integer)
    e_recomended  = db.Column(db.Integer)
    e_position_eng = db.Column(db.String(255))
    e_salary_base = db.Column(db.Integer)
    e_recruiter = db.Column(db.String(255))
    e_days_to_hire = db.Column(db.Integer)
    e_commute = db.Column(db.Float)
    e_entrance_type = db.Column(db.Integer)
    e_source = db.Column(db.String(255))
    e_date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    predictions = db.relationship("Candidate_predictions", backref="Candidate", lazy=True)
    
    def __init__(self, e_id, e_name, e_age, e_gender, e_recomended, e_position_eng, e_salary_base, e_recruiter, e_days_to_hire, e_commute, e_entrance_type, e_source):
        self.e_id = e_id
        self.e_name = e_name
        self.e_age = e_age
        self.e_gender = e_gender
        self.e_recomended = e_recomended
        self.e_position_eng = e_position_eng
        self.e_salary_base = e_salary_base
        self.e_recruiter = e_recruiter
        self.e_days_to_hire = e_days_to_hire
        self.e_commute = e_commute
        self.e_entrance_type = e_entrance_type
        self.e_source = e_source
    
    def __repr__(self):
        return "Candidate {e_name}".format(e_name=self.e_name)
    
class Candidate_predictions(db.Model):
    candidates = db.relationship(Candidate)

    p_id = db.Column(db.Integer, primary_key=True)
    p_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    e_recruiter = db.Column(db.String(255))
    e_id = db.Column(db.Integer, db.ForeignKey("candidates.e_id"), nullable=False)
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
    
    
"""
'e_position_eng',
'e_salary_base',
'u_department',
'u_unit',
'u_ntt',
'e_age',
'e_gender',
'u_tl_tenure',
'u_tl_age',
'u_tl_gender',
'u_hires_week',
'u_exits_week',
'u_hires_month',
'u_exits_month',
'u_headcount',
'u_age_mean',
'u_tenure_mean',
'u_gender_average',
'e_entrance_type',
'e_source',
'e_days_to_hire',
'e_recomended',
'r_age',
'r_tenure',
'r_level',
'u_tl_active',
'e_commute',
'e_position_eng_DC employee',
'u_department_B2B',
'u_department_Shift_1',
'u_department_Shift_2',
'u_department_Shift_3',
'u_department_Shift_4',
'u_department_Trouble_Shooting',
'u_unit_B2B_Area',
'u_unit_Inventarization_Area',
'u_unit_Loading_Area',
'u_unit_New_Arrivals_Area',
'u_unit_Pack_Item_Area',
'u_unit_Packing_Area',
'u_unit_Picking_Area',
'u_unit_Putaway_Area',
'u_unit_Return_Area',
'u_unit_Sorting_Area',
'u_unit_Trouble_Area',
'u_unit_Unpacking_Area',
'e_source_superjob',
'e_position_eng_DC_employee',
'e_position_eng_Leading_DC_employee',
'e_position_eng_Senior_DC_employee',
'e_source_headhunter',
'e_source_hh.ru',
'e_source_job-mo',
'e_source_lamoda',
'e_source_other',
'e_source_rabota',
'e_source_ref',
'e_source_zarplata',
'p_success_probability'
"""    