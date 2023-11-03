from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, Model


class CarOwner(Model):
    name = CharField(max_length=30)
    surname = CharField(max_length=30)
    date_of_birth = DateTimeField()


class DriversLicence(Model):
    owner = ForeignKey(CarOwner, CASCADE)
    number = CharField(max_length=10)
    _type = CharField(max_length=10)
    issue_date = DateTimeField()


class Car(Model):
    number = CharField(max_length=15)
    model = CharField(max_length=20)
    color = CharField(max_length=30)


class Ownership(Model):
    owner = ForeignKey(CarOwner, CASCADE)
    car = ForeignKey(Car, CASCADE)
    start_date = DateTimeField()
    end_date = DateTimeField(null=True, blank=True)
