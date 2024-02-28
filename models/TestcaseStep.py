from db import db

class TestcaseStepModel(db.Model):
    __tablename__ = "testcase_steps"
 
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())

    testcase_id = db.Column(db.Integer, db.ForeignKey("testcases.id"), unique=False, nullable=False)
    testcase = db.relationship("TestcaseModel", back_populates="testcase_steps")