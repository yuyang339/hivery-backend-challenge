from urllib import parse
import json
import falcon

from paranuara.resources.people import PeopleController
from paranuara.models.People import People

VALID_Q = ['isalive', 'eyecolor']

class FriendController():
    @staticmethod
    def getCommonFriends(people_aid, people_bid, query):
        peopleControllerA = PeopleController(id=people_aid)
        peopleControllerB = PeopleController(id=people_bid)

        friendsOfA = set(peopleControllerA.getFriendIds())
        friendsOfB = set(peopleControllerB.getFriendIds())
        friendsOfAB = list(friendsOfA.intersection(friendsOfB))

        if len(query_string):
            has_died = not query['isalive']
            friends = People.objects(index__in=friendsOfAB, eyeColor=query['eyecolor'].lower(), has_died=has_died)
        else:
            friends = People.objects(index__in=friendsOfAB)

        data = {
            "PeopleA": {
                "name": peopleControllerA.username,
                "age": peopleControllerA.age,
                "phone": peopleControllerA.phone,
                "address": peopleControllerA.address
            },
            "PeopleB": {
                "name": peopleControllerB.username,
                "age": peopleControllerB.age,
                "phone": peopleControllerB.phone,
                "address": peopleControllerB.address
            },
            "Friends": []
        }
        for friend in friends:
            data["Friends"].append({
                "name": friend.name,
                "eyecolor": friend.eyeColor,
                "isAlive": not friend.has_died,
                "age": friend.age,
                "phone": friend.phone,
                "address": friend.address
            })

        return data

class FriendResource(object):
    def on_get(self, req, resp, people_aid, people_bid):
        query_string = req.query_string
        valid_query = {}
        for query_k, query_v in parse.parse_qsl(query_string):
            if query_k in VALID_Q:
                valid_query[query_k] = query_v
            else:
                raise falcon.HTTPBadRequest("Please provide valid query " + str(VALID_Q))

        try:
            data = FriendController.getCommonFriends(people_aid, people_bid, valid_query)
        except:
            raise falcon.HTTPBadRequest("People not found")

        resp.body = json.dumps(data)
        resp.status = falcon.HTTP_200
        