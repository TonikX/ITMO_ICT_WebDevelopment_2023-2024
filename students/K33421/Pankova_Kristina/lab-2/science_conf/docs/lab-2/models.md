## Models
Модель посетителя конференции
```python
class ConferenceGuest(AbstractUser):
    birth_date = models.DateField(null=True)
    conferences = models.ManyToManyField('Conference', through='ConferenceAttendance', through_fields=('guest', 'conference'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['id']
```

Модель конференции
```python
class Conference(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=2,
        choices=CONFERENCE_TYPE_CHOICES,
        default="SC",
    )
    date_begin = models.DateField(null=True)
    date_end = models.DateField(null=True)
    city = models.CharField(max_length=100, null=True)
    place_description = models.CharField(max_length=400, null=True)
    payment_fee = models.IntegerField(null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    conditions = models.CharField(max_length=500, null=True)
    guests = models.ManyToManyField('ConferenceGuest', through='ConferenceAttendance', through_fields=('conference', 'guest'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['id']
```

Модель посетителя на конкретной конференции, нужна для обозначения роли
```python
class ConferenceAttendance(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    guest = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=2,
        choices=CONFERENCE_ROLE_CHOICES,
        default="AT",
    )
    form_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='form_author')


    def __str__(self):
        return f'{self.guest} at {self.conference}'

    class Meta:
        ordering = ['id']
```

Модель для комментариев о конференции
```python
class ConferenceComments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    text = models.CharField(max_length=555)
    type = models.IntegerField(
        choices=RATING_CHOICES,
        default=None,
        null=True
    )
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s comment of {self.conference}"

    class Meta:
        ordering = ['id']
```

Модель лекции на конференции
```python
class ConferenceLectures(models.Model):
    lecturer = models.ForeignKey(ConferenceAttendance, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    given_at = models.DateField(null=True)
    is_recommended = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.lecturer}'s lecture at {self.conference}"

    class Meta:
        ordering = ['id']
```