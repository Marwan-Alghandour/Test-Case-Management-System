from marshmallow import Schema, fields, validate

class PlainTestcaseStepSchema(Schema):
    id = fields.Str(dump_only=True)
    input = fields.Str(required=True, error_messages={"required": {"message": "'input' field required", "code": 400}})
    type = fields.Str(required=True, error_messages={"required": {"message": "'type' field required", "code": 400}})
    created_at = fields.DateTime(dump_only=True)

class PlainTestcaseSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True, error_messages={"required": {"message": "'title' field required", "code": 400}})
    description = fields.Str(required=True, error_messages={"required": {"message": "'description' field required", "code": 400}})
    expected_output = fields.Str(required=True, error_messages={"required": {"message": "'expected_output' field required", "code": 400}})
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class TestcaseStepSchema(PlainTestcaseStepSchema):
    testcase_id = fields.Str(dump_only=True)
    testcase = fields.Nested(PlainTestcaseSchema(), dump_only=True)

class TestcaseUpdateSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    expected_output = fields.Str()
    testcase_steps = fields.List(fields.Nested(PlainTestcaseStepSchema()), validate=validate.Length(min=1,error="'steps' field can not be empty"))

class PlainSubjectSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, error_messages={"required": {"message": "'name' field required", "code": 400}})
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class SubjectUpdateSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": {"message": "'name' field required", "code": 400}})

class SubjectSchema(PlainSubjectSchema):
    testcases = fields.List(fields.Nested(PlainTestcaseSchema()), dump_only=True)

class TestcaseSchema(PlainTestcaseSchema):
    subjects = fields.List(fields.Nested(PlainSubjectSchema()), dump_only=True)
    testcase_steps = fields.List(fields.Nested(PlainTestcaseStepSchema()), required=True, validate=validate.Length(min=1,error="'steps' field can not be empty"), error_messages={"required": {"message": "'steps' field required", "code": 400}})

class SubjectAndTestcaseSchema(Schema):
    id = fields.Str(dump_only=True)
    subject = fields.Nested(PlainSubjectSchema(), dump_only=True)
    testcase = fields.Nested(PlainTestcaseSchema(), dump_only=True)
    status = fields.Boolean(required=True, error_messages={"required": {"message": "'status' field required", "code": 400}})
    actual_output = fields.Str(required=True, error_messages={"required": {"message": "'actual_output' field required", "code": 400}})
    comment = fields.Str(required=True, error_messages={"required": {"message": "'comment' field required", "code": 400}})
    created_at = fields.DateTime(dump_only=True)