import falcon
from mongoengine import connect

from paranuara.resources import company, people, friend

class ParanuaraService(falcon.API):
    def __init__(self, config=None):
        super(ParanuaraService, self).__init__()

        if config:
            connect('paranuara', host=config.mongo["host"], port=config.mongo["port"])

        company_res = company.CompanyResource()
        people_res = people.PeopleResource()
        friend_res = friend.FriendResource()

        # Build routes
        self.add_route("/api/company/{company_id}/employees", company_res)
        self.add_route("/api/people/{people_id}/favoritefood", people_res)
        self.add_route("/api/commonfriend/{people_aid}/{people_bid}", friend_res)

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass

    @staticmethod
    def create():
        return ParanuaraService()
