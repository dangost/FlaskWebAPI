from marshmallow import fields, Schema


class CustomerCompanySchema(Schema):
    CompanyName = fields.String(attribute="CompanyName")

    CompanyCreditLimit = fields.String(attribute="CompanyCreditLimit")

    CreditLimitCurrency = fields.String(attribute="CreditLimitCurrency")



