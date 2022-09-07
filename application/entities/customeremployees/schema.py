from marshmallow import fields, Schema


class CustomerEmployeeSchema(Schema):
    CustomerEmployeeId = fields.Integer(attribute="CustomerEmployeeId")

    CompanyId = fields.Integer(attribute="CompanyId")

    BadgeNumber = fields.String(attribute="BadgeNumber")

    JobTitle = fields.String(attribute="JobTitle")

    Department = fields.String(attribute="Department")

    CreditLimit = fields.Integer(attribute="CreditLimit")

    CreditLimitCurrency = fields.Integer(attribute="CreditLimitCurrency")
