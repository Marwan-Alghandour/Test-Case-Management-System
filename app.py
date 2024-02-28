from flask import Flask
from flask_smorest import Api
from resources.testcase import blueprint as TestcaseBlueprint
from resources.subject import blueprint as SubjectBlueprint
from db import db
import models

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Testcases REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(TestcaseBlueprint)
    api.register_blueprint(SubjectBlueprint)

    return app