from marshmallow import fields, Schema


class EmploymentJobsSchema(Schema):
    CountriesCountryId = fields.Integer(attribute="CountriesCountryId")

    JobTitle = fields.String(attribute="JobTitle")

    MinSalary = fields.Integer(attribute="MinSalary")

    MaxSalary = fields.Integer(attribute="MaxSalary")



