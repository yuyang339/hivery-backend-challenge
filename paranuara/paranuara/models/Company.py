from mongoengine import StringField, IntField, Document

class Company(Document):
    index = IntField()
    company = StringField()