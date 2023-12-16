# Модели

### Доктор

```python
class Doctor(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=50)
    Contacts = models.CharField(max_length=100)
```

### Пациент

```python
class Patient(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Birth_Date = models.DateField()
    Sex = models.CharField(max_length=10)
    Contacts = models.CharField(max_length=100)
```

### Визиты

```python
class Visit(models.Model):
    ID = models.AutoField(primary_key=True)
    ID_Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ID_Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Diagnoz = models.TextField()
    Appointment = models.TextField()
    ID_Service = models.ForeignKey(Service, on_delete=models.CASCADE)
```

### Услуги

```python
class Service(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
```

### Оплата

```python
class Payment(models.Model):
    ID = models.AutoField(primary_key=True)
    ID_Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Date = models.DateField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
```