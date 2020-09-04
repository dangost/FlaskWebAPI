from marshmallow import fields, Schema


class EmploymentJobsSchema(Schema):
    HRJobId = fields.Integer(attribute="HRJobId")

    CountriesCountryId = fields.Integer(attribute="CountriesCountryId")

    JobTitle = fields.String(attribute="JobTitle")

    MinSalary = fields.Integer(attribute="MinSalary")

    MaxSalary = fields.Integer(attribute="MaxSalary")



