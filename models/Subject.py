from db import db
 
class SubjectModel(db.Model):
    __tablename__ = "subjects"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

    testcases = db.relationship('TestcaseModel', secondary="subjects_testcases", back_populates='subjects')