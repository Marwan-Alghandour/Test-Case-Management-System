from db import db
 
class TestcaseModel(db.Model):
    __tablename__ = "testcases"
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    expected_output = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())

    testcase_steps = db.relationship("TestcaseStepModel", back_populates="testcase", lazy="dynamic", cascade="all, delete")

    subjects = db.relationship('SubjectModel', secondary="subjects_testcases", back_populates='testcases')