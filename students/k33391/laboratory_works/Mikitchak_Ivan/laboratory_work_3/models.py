from django.db import models

# Create your models here.
class Agent(models.Model):
    full_name = models.CharField(max_length=50)
    passport_data = models.CharField(max_length=50)
    contact_data = models.CharField(max_length=50)
    

class NaturalPerson(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    

class Specialization(models.Model):
    name = models.CharField(max_length=50)


class LegalPerson(models.Model):
    full_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    bank_credentials = models.CharField(max_length=50)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    

class NaturalPersonContract(models.Model):
    since = models.DateField()
    till = models.DateField()
    premium = models.IntegerField()
    payment = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    natural_person = models.ForeignKey(NaturalPerson, on_delete=models.CASCADE)
    

class LegalPersonContract(models.Model):
    since = models.DateField()
    till = models.DateField()
    low_premium = models.IntegerField()
    medium_premium = models.IntegerField()
    high_premium = models.IntegerField()
    low_payment = models.IntegerField()
    medium_payment = models.IntegerField()
    high_payment = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    legal_person = models.ForeignKey(LegalPerson, on_delete=models.CASCADE)


class Employee(models.Model):
    RISK_CATEGORY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    risk_category = models.CharField(max_length=20, choices=RISK_CATEGORY_CHOICES)
    contract = models.ForeignKey(LegalPersonContract, on_delete=models.CASCADE)


class InsuredEvent(models.Model):
    EVENT_CONTRACT_TYPE_CHOICES = [
        ('natural_person', 'Natural Person'),
        ('legal_person', 'Legal Person'),
    ]
    
    date = models.DateField()
    cause = models.CharField(max_length=100)
    payment = models.IntegerField()
    contract_type = models.CharField(max_length=20, choices=EVENT_CONTRACT_TYPE_CHOICES)
    contract_id = models.IntegerField()

    def get_contract(self):
        if self.contract_type == 'natural_person':
            return NaturalPersonContract.objects.get(natural_person_contract_id=self.contract_id)
        elif self.contract_type == 'legal_person':
            return LegalPersonContract.objects.get(legal_person_contract_id=self.contract_id)
        else:
            return None
     