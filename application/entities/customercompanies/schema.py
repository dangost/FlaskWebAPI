from marshmallow import fields, Schema


class CustomerCompanySchema(Schema):
    CompanyId = fields.Integer(attribute="CompanyId")

    CompanyName = fields.String(attribute="CompanyName")

    CompanyCreditLimit = fields.String(attribute="CompanyCreditLimit")

    CreditLimitCurrency = fields.String(attribute="CreditLimitCurrency")



