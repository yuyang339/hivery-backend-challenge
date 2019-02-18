from mongoengine import StringField, IntField, Document, BooleanField, ListField

class People(Document):
    index = IntField()
    guid = StringField()
    has_died = BooleanField()
    balance = StringField()
    picture = StringField()
    age = IntField()
    eyeColor = StringField()
    name = StringField()
    gender = StringField()
    company_id = IntField()
    email = StringField()
    phone = StringField()
    address = StringField()
    about = StringField()
    registered = StringField()
    tags = ListField()
    friends = ListField()
    greeting = StringField()
    favouriteFood = ListField()
    
