from hroracle import db
from datetime import datetime


#flask db init
#flask db migrate -m "message"
#flask db upgrade




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

    __tablename__ = "candidate_predictions"
    
    p_id = db.Column(db.Integer, primary_key=True)
    e_id = db.Column(db.Integer, db.ForeignKey('candidates.e_id'), nullable=False)
    e_name = db.Column(db.String(255))
    r_id = db.Column(db.String(255))
    u_id = db.Column(db.String(255))
    e_recruiter = db.Column(db.String(255))
    e_position_eng = db.Column(db.String(255))
    e_date_entered = db.Column(db.String(255))
    e_start_day = db.Column(db.Integer)
    e_start_month = db.Column(db.Integer)
    e_start_year = db.Column(db.Integer)
    e_start_weekday = db.Column(db.Integer)
    e_salary_base = db.Column(db.Integer)
    u_department = db.Column(db.String(255))
    u_unit = db.Column(db.String(255))
    u_ntt = db.Column(db.Integer)
    e_age = db.Column(db.Integer)
    e_gender = db.Column(db.Integer)
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
    e_entrance_type = db.Column(db.Integer)
    e_source = db.Column(db.String(255))
    e_days_to_hire = db.Column(db.Integer)
    e_recomended = db.Column(db.Integer)
    r_age = db.Column(db.Integer)
    r_tenure = db.Column(db.Integer)
    r_level = db.Column(db.Integer)
    u_tl_active = db.Column(db.Integer)
    e_commute = db.Column(db.Float)
    e_position_eng_DC_employee = db.Column(db.Integer)
    u_department_B2B = db.Column(db.Integer)
    u_department_Shift_1 = db.Column(db.Integer)
    u_department_Shift_2 = db.Column(db.Integer)
    u_department_Shift_3 = db.Column(db.Integer)
    u_department_Shift_4 = db.Column(db.Integer)
    u_department_Trouble_Shooting = db.Column(db.Integer)
    u_unit_B2B_Area = db.Column(db.Integer)
    u_unit_Inventarization_Area = db.Column(db.Integer)
    u_unit_Loading_Area = db.Column(db.Integer)
    u_unit_New_Arrivals_Area = db.Column(db.Integer)
    u_unit_Pack_Item_Area = db.Column(db.Integer)
    u_unit_Packing_Area = db.Column(db.Integer)
    u_unit_Picking_Area = db.Column(db.Integer)
    u_unit_Putaway_Area = db.Column(db.Integer)
    u_unit_Return_Area = db.Column(db.Integer)
    u_unit_Sorting_Area = db.Column(db.Integer)
    u_unit_Trouble_Area = db.Column(db.Integer)
    u_unit_Unpacking_Area = db.Column(db.Integer)
    e_source_superjob = db.Column(db.Integer)
    e_position_eng_DC_employee = db.Column(db.Integer)
    e_position_eng_Leading_DC_employee = db.Column(db.Integer)
    e_position_eng_Senior_DC_employee = db.Column(db.Integer)
    e_source_headhunter = db.Column(db.Integer)
    e_source_job_mo = db.Column(db.Integer)
    e_source_lamoda = db.Column(db.Integer)
    e_source_other = db.Column(db.Integer)
    e_source_rabota = db.Column(db.Integer)
    e_source_ref = db.Column(db.Integer)
    e_source_zarplata = db.Column(db.Integer)
    p_success_probability = db.Column(db.Float)
    e_unit_name = db.Column(db.String(255))
    
    
class Recruiter(db.Model):
    
    __tablename__ = "recruiters"
    
    r_id = db.Column(db.String(255), primary_key=True)
    e_recruiter = db.Column(db.String(255))
    r_age = db.Column(db.Integer)
    r_tenure = db.Column(db.Integer)
    r_level = db.Column(db.Integer)    

class Unit(db.Model):

    __tablename__ = "units"
    
    u_id = db.Column(db.Integer, primary_key=True)
    e_unit_name = db.Column(db.String(255))
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
    