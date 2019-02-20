import falcon
import json
from paranuara.models.People import People
from paranuara.helpers.common import isFruit, isVegetable
class PeopleController(object):
    def __init__(self, people_id=None, name=None):
        try:
            if people_id:
                people = People.objects.get(index=people_id)
            elif name:
                people = People.objects.get(name=name)
            else:
                raise
        except:
            raise
        
        self.model = people
        self.people_id = people_id
    
    def getFavoriteFood(self):
        data = {
            "username": self.username,
            "age": self.age,
            "fruits": [],
            "vegetables": [],
        }
        for food in self.model.favouriteFood:
            if isFruit(food):
                data["fruits"].append(food)
            if isVegetable(food):
                data["vegetables"].append(food)

        return data

    @property
    def username(self):
        return self.model.name

    @property
    def age(self):
        return self.model.age

    @property
    def address(self):
        return self.model.address

    @property
    def phone(self):
        return self.model.phone

    def getFriendIds(self):
        return [friend["index"] for friend in self.model.friends if int(self.people_id) != friend["index"]]

class PeopleResource(object):
    def on_get(self, req, resp, people_id):
        """Handles GET requests"""
        try:
            peopleController = PeopleController(people_id=people_id)
        except:
            raise falcon.HTTPBadRequest("This people is not existed")
        
        resp.body = json.dumps(peopleController.getFavoriteFood())
        resp.status = falcon.HTTP_200
