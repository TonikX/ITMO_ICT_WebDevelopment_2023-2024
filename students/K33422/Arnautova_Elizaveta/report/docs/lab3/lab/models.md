**Models:** 

Горы
```
class Mountain(models.Model):
    class Meta:
        db_table = 'mountain'

    name = models.CharField(max_length=50)
    height = models.IntegerField()
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
```

Маршрут
```
class Route(models.Model):
    class Meta:
        db_table = 'route'
        unique_together = [['mountain', 'description']]

    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return self.mountain.name + " " + str(self.id)
```

Восхождение
```
class Ascension(models.Model):
    class Meta:
        db_table = 'ascension'

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    start_date = models.DateField()
    planned_end_date = models.DateField()
    actual_end_date = models.DateField(null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.route.mountain.name + " " + str(self.route) + "." + str(self.id)
```

Группа, отправившаяся в это самое восхождение
```
class Group(models.Model):
    class Meta:
        db_table = 'group'

    ascension = models.ForeignKey(Ascension, on_delete=models.CASCADE)
    result = models.CharField(max_length=50, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    climbers = models.ManyToManyField('Climber', through='AscentParticipation')

    def __str__(self):
        return str(self.id)
```

Турклуб
```
class Club(models.Model):
    class Meta:
        db_table = 'club'

    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
```

Альпинист
```
class Climber(models.Model):
    class Meta:
        db_table = 'climber'

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    groups = models.ManyToManyField('Group', through='AscentParticipation')

    def __str__(self):
        return self.last_name + " " + self.first_name
```

Участие в восхождении -- информация о конкретном альпинисте в конкретном восхождении
```
class AscentParticipation(models.Model):
    class Meta:
        db_table = 'ascent_participation'
        unique_together = [['climber', 'group']]

    climber = models.ForeignKey(Climber, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    result = models.CharField(max_length=50)
    comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.climber.last_name + " " + self.climber.first_name + " group " + str(self.group)
```