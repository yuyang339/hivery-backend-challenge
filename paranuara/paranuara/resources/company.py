import falcon
import json
from paranuara.models.People import People

class CompanyController(object):
    def __init__(self, id):
        self.id = int(id)

    @staticmethod
    def getAllEmployees(company_id):
        employees = People.objects(company_id=company_id)

        data = {}
        for e in employees:
            data[e.index] = {
                'name': e.name,
                'registeredDate': e.registered,
            }

        return data


class CompanyResource(object):
    def on_get(self, req, resp, company_id):
        resp.body = json.dumps(CompanyController.getAllEmployees(company_id))
        resp.status = falcon.HTTP_200
