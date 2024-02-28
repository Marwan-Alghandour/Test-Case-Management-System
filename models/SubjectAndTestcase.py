from db import db

class SubjectAndTestcaseModel(db.Model):
    __tablename__ = "subjects_testcases"
 
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))
    testcase_id = db.Column(db.Integer, db.ForeignKey("testcases.id"))
    status = db.Column(db.Boolean, nullable=False)
    actual_output = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())