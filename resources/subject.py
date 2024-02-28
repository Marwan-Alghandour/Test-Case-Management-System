from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import SubjectSchema, SubjectUpdateSchema, SubjectAndTestcaseSchema
from models import SubjectModel, TestcaseModel, SubjectAndTestcaseModel
from db import db

blueprint = Blueprint("subjects", __name__, description="Operations on subjects")

@blueprint.route("/subject")
class SubjectList(MethodView):

    @blueprint.arguments(SubjectSchema)
    @blueprint.response(201, SubjectSchema)
    def post(self, subject_data):
        subject = SubjectModel(**subject_data)
        try:
            db.session.add(subject)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Subject name already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while inserting the subject")
        return subject
    
    @blueprint.response(200, SubjectSchema(many=True))
    def get(self):
        return list(SubjectModel.query.all())
    
@blueprint.route("/subject/<string:subject_id>")
class Testcase(MethodView):

    @blueprint.response(200, SubjectSchema)
    def get(self, subject_id):
        subject = SubjectModel.query.get_or_404(subject_id)
        return subject

    @blueprint.arguments(SubjectUpdateSchema)
    @blueprint.response(200, SubjectSchema)
    def put(self, subject_data, subject_id):
        subject = SubjectModel.query.get_or_404(subject_id)
        subject.name = subject_data["name"]
        try:
            db.session.merge(subject)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Subject name already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while updating the subject")
        return subject
        

    def delete(self, subject_id):
        subject = SubjectModel.query.get_or_404(subject_id)
        try:
            db.session.delete(subject)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Error occured while updating the subject")
        return {"message": "Subject deleted"}


@blueprint.route("/subject/<string:subject_id>/testcase/<string:testcase_id>")
class SubjectTestcaseList(MethodView):

    @blueprint.arguments(SubjectAndTestcaseSchema)
    @blueprint.response(201, SubjectAndTestcaseSchema)
    def post(self, subject_testcase_data, subject_id, testcase_id):     
        SubjectModel.query.get_or_404(subject_id)
        TestcaseModel.query.get_or_404(testcase_id)
        test = SubjectAndTestcaseModel(subject_id=subject_id, testcase_id=testcase_id, **subject_testcase_data)
        try:
            db.session.add(test)
            db.session.commit()    
        except SQLAlchemyError:
            abort(500, message="Error occured while inserting the execution result")

        return test
    
    @blueprint.response(200, SubjectAndTestcaseSchema(many=True))
    def get(self, subject_id, testcase_id):
        SubjectModel.query.get_or_404(subject_id)
        TestcaseModel.query.get_or_404(testcase_id)
        return list(SubjectAndTestcaseModel.query.filter(SubjectAndTestcaseModel.subject_id == subject_id and SubjectAndTestcaseModel.testcase_id == testcase_id))