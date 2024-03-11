from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Company(models.Model):
    code = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    address = models.TextField()
    bank_details = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Agent(models.Model):
    full_name = models.CharField(max_length=100)
    passport_data = models.CharField(max_length=20)
    contact_details = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class AgentContract(models.Model):
    agent = models.ForeignKey(
        Agent, related_name="agent_contract", on_delete=models.CASCADE
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    active_flag = models.BooleanField(default=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date")

    def __str__(self):
        return f"{self.agent.full_name} contract"


class Employee(models.Model):
    RISK_CATEGORIES = (
        ("first", "первая"),
        ("second", "вторая"),
        ("third", "третья"),
    )

    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    risk_category = models.CharField(max_length=20, choices=RISK_CATEGORIES)
    company = models.ForeignKey(
        Company, related_name="employees", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.full_name


class CollectiveAgreement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    # date_of_agreement = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_payout = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"collective {self.agent.full_name} for {self.company.full_name}"

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date")

    def is_active(self):
        return self.start_date <= timezone.localtime() <= self.end_date


class IndividualAgreement(models.Model):
    # company = models.ForeignKey(Company, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # date_of_agreement = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_payout = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"individual {self.agent.full_name} for {self.employee.full_name}"

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date")

    def is_active(self):
        return self.start_date <= timezone.localtime() <= self.end_date


class CollectiveInsuranceClaim(models.Model):
    agreement = models.ForeignKey(CollectiveAgreement, on_delete=models.CASCADE)
    date_of_claim = models.DateField()
    cause = models.TextField()
    decision = models.CharField(max_length=50)
    payout_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"collective case {self.date_of_claim}"


class IndividualInsuranceClaim(models.Model):
    employee = models.ForeignKey(IndividualAgreement, on_delete=models.CASCADE)
    date_of_claim = models.DateField()
    cause = models.TextField()
    decision = models.CharField(max_length=50)
    payout_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"individual case {self.date_of_claim}"






## Add Agent Contract
## Add Insurace Claim
## Add all basic model!!

## Распространить отображения в Report
## И договора, и страховые случаи для компании

