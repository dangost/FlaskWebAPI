from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import EmploymentJobsSchema
from .service import EmploymentJobsService
from .model import EmploymentJobs
from .interface import EmploymentJobsInterface

api = Namespace("EmploymentJobs", description="Single namespace, single entity")

service = EmploymentJobsService

@api.route("/")
class EmploymentJobsResource(Resource):

    @responds(schema=EmploymentJobsSchema(many=True))
    def get(self) -> List[EmploymentJobs]:
        
        return service.get_all(self)

    @accepts(schema=EmploymentJobsSchema, api=api)
    @responds(schema=EmploymentJobsSchema)
    def post(self) -> EmploymentJobs:
        obj: dict = request.parsed_obj
        return service.create(self, obj)


@api.route("/<int:HRJobId>")
@api.param("EmploymentJobsId", "EmploymentJobs database ID")
class EmploymentJobsIdResource(Resource):
    @responds(schema=EmploymentJobsSchema)
    def get(self, HRJobId: int) -> EmploymentJobs:
        return service.get_by_id(self, HRJobId)

    def delete(self, HRJobId: int) -> Response:
        from flask import jsonify

        id: int = service.delete_by_id(self, HRJobId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=EmploymentJobsSchema, api=api)
    @responds(schema=EmploymentJobsSchema)
    def put(self, HRJobId: int) -> EmploymentJobs:

        changes: EmploymentJobsInterface = request.parsed_obj
        employmentjobs = service.get_by_id(self, HRJobId)
        return service.update(self, employmentjobs, changes)

