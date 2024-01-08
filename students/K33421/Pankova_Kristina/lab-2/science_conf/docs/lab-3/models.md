# Файл models.py


Модели для пользователей - клиент и владелец бизнеса.
```python
class Customer(User):
    phone_number = models.CharField(max_length=11)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['id']

class SalonOwner(User):
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['id']
```
Модель для салона (бизнеса) и комментариев к нему:
```python
class Salon(models.Model):
    owner = models.ForeignKey(SalonOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    type = models.CharField(
        max_length=2,
        choices=SALON_TYPE_CHOICES,
        default="SC",
    )
    date_registered = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['id']

class SalonComments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    text = models.CharField(max_length=555)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=None,
        null=True
    )
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}'s comment of {self.salon}"

    class Meta:
        ordering = ['id']
```

Модель для услуг в салоне (Например, стрижка)
```python

class SalonService(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}' at {self.salon}"

    class Meta:
        ordering = ['id']
```

Модель для записи на услугу в салоне и для комменатриев к услугам.

```python
class SalonAppointment(models.Model):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(SalonService, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} at {self.salon}'

    class Meta:
        ordering = ['id']


class SalonServiceComments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salon_service = models.ForeignKey(SalonService, on_delete=models.CASCADE)
    text = models.CharField(max_length=555)
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=None,
        null=True
    )
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}'s comment of {self.salon_service}"

    class Meta:
        ordering = ['id']


```