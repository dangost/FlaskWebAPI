from marshmallow import fields, Schema


class EmploymentSchema(Schema):
    PersonId = fields.Integer(attribute="PersonId")

    HRJobId = fields.Integer(attribute="HRJobId")

    ManagerEmployeeId = fields.Integer(attribute="ManagerEmployeeId")

    StartDate = fields.String(attribute="StartDate")

    EndDate = fields.String(attribute="EndDate")

    Salary = fields.String(attribute="Salary")

    CommissionPercent = fields.Integer(attribute="CommissionPercent")

    EmploymentCol = fields.String(attribute="EmploymentCol")



