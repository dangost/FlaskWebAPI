from marshmallow import fields, Schema


class CustomerSchema(Schema):
    CustomerId = fields.Integer(attribute="CustomerId")

    PersonId = fields.Integer(attribute="PersonId")

    CustomEmployeeId = fields.Integer(attribute="CustomEmployeeId")

    AccountMgrId = fields.Integer(attribute="AccountMgrId")

    IncomeLevel = fields.Integer(attribute="IncomeLevel")



