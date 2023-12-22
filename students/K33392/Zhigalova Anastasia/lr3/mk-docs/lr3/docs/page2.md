# models.py

``` 
from django.db import models

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    date_of_start = models.DateField()
    date_of_end = models.DateField()
    contract_data = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name

class Cabinet(models.Model):
    name = models.CharField(max_length=50)
    work_schedule = models.CharField(max_length=100)
    responsible = models.CharField(max_length=50)
    internal_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    medical_card_number = models.CharField(max_length=20)

    def __str__(self):
        return self.last_name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    diagnosis = models.CharField(max_length=100)
    current_condition = models.CharField(max_length=100)
    treatment_recommendations = models.CharField(max_length=100)

    def __str__(self):
        return self.diagnosis

class Payment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class MedicalService(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

```