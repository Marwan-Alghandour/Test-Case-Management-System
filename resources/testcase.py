from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import TestcaseSchema, TestcaseUpdateSchema
from models import TestcaseModel, TestcaseStepModel
from db import db

blueprint = Blueprint("testcases", __name__, description="Operations on testcases")

@blueprint.route("/testcase")
class TestcaseList(MethodView):

    @blueprint.arguments(TestcaseSchema)
    @blueprint.response(201, TestcaseSchema)
    def post(self, testcase_data):
        steps = testcase_data["testcase_steps"]
        del testcase_data["testcase_steps"]
        testcase = TestcaseModel(**testcase_data)
        for step in steps:
            step = TestcaseStepModel(**step)
            testcase.testcase_steps.append(step)
        try:
            db.session.add(testcase)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Testcase title already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while inserting the testcase")
        return testcase
    
    @blueprint.response(200, TestcaseSchema(many=True))
    def get(self):
        return list(TestcaseModel.query.all())
    
@blueprint.route("/testcase/<string:testcase_id>")
class Testcase(MethodView):

    @blueprint.response(200, TestcaseSchema)
    def get(self, testcase_id):
        testcase = TestcaseModel.query.get_or_404(testcase_id)
        return testcase

    @blueprint.arguments(TestcaseUpdateSchema)
    @blueprint.response(200, TestcaseSchema)
    def put(self, testcase_data, testcase_id):
        testcase = TestcaseModel.query.get_or_404(testcase_id) 
        if "testcase_steps" in testcase_data:
            TestcaseStepModel.query.filter_by(testcase_id=testcase_id).delete()
        
        steps = testcase_data["testcase_steps"]
        del testcase_data["testcase_steps"]

        for key in testcase_data:
            setattr(testcase, key, testcase_data[key])
        
        for step in steps:
            step = TestcaseStepModel(**step)
            testcase.testcase_steps.append(step)
    
        try:
            db.session.merge(testcase)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Testcase title already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while updating the testcase")

        return testcase
            

    def delete(self, testcase_id):
        testcase = TestcaseModel.query.get_or_404(testcase_id)
        try:
            db.session.delete(testcase)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occured while updating the testcase")
        return {"message": "Testcase deleted"}