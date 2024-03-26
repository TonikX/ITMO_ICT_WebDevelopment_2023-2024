from django.db import models
from django.contrib.auth.models import User


class Individual(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, default=None)
    passport = models.PositiveBigIntegerField()
    phone = models.PositiveBigIntegerField()
    address = models.CharField(max_length=255)


class Type(models.Model):
    title = models.CharField(max_length=255)
    summ = models.PositiveSmallIntegerField()


class Organization(models.Model):
    types = (
        ('медицинское учреждение', 'медицинское учреждение'),
        ('автотранспортное предприятие', 'автотранспортное предприятие'),
        ('учебное заведение', 'учебное заведение'),
        ('другое', 'другое')
    )

    code = models.PositiveIntegerField(primary_key=True)
    fullname = models.CharField(max_length=255)
    shortname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bank_number = models.PositiveBigIntegerField()
    type = models.CharField(max_length=35, choices=types)


class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, default=None)
    age = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Type, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, to_field='code')


class InsureOrganization(models.Model):
    fullname = models.CharField(max_length=255)
    shortname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)


class InsureAgent(User):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    passport = models.PositiveBigIntegerField()
    phone = models.PositiveBigIntegerField()
    address = models.CharField(max_length=255)
    insureorganization = models.ForeignKey(InsureOrganization, on_delete=models.CASCADE)


class Contract(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    organization = models.ForeignKey(Organization, null=True, on_delete=models.CASCADE, default=None)
    client = models.ForeignKey(Individual, null=True, on_delete=models.CASCADE, default=None)
    agent = models.ForeignKey(InsureAgent, on_delete=models.CASCADE)


class InsuranceCase(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=1023)
    damage_summ = models.PositiveIntegerField()
    payment = models.PositiveIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
