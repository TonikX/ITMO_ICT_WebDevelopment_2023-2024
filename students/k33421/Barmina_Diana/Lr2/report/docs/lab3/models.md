# База данных

Задание 15
Создать программную систему, предназначенную для администратора
альпинистского клуба. Альпинистский клуб организует восхождения в разных точках
мира. Система должна обеспечить сохранение информации о хронике восхождений.
Для каждого восхождения формируется группа. В состав группы могут входить
альпинисты из других клубов. Поэтому нужно иметь информацию о каждом клубе
(название, страна, город, контактное лицо, e-mail, телефон). Необходимо иметь описание
маршрута и продолжительность восхождения. Необходимо обеспечить сохранение
даты/времени начала и завершения каждого восхождения (планируемого и фактического),
имен и адресов участвовавших в нем альпинистов, названия и высоты горы, страны и
района, где эта гора расположена. После завершения восхождения фиксируется
информация об успешности восхождения для каждого участника и группы в целом. При
возникновении нештатных ситуаций необходимо указать для каждого участника, что
случилось 

**Alpinist - пользователь**

```

class Alpinist(AbstractUser):

    experience_level_types = (
        ('Новичок', 'Новичок'),
        ('Продвинутый', 'Продвинутый'),
        ('Профи', 'Профи'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    document = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=11, choices=experience_level_types)
    clubs = models.ManyToManyField('Club', through='ClubMembership')
    climbings = models.ManyToManyField('Climbing', through='Participating')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'email', 'document', 'birth_date', 'address', 'experience_level']

```
**Club**

```

class Club(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    alpinists = models.ManyToManyField('Alpinist', through='ClubMembership')

    def __str__(self):
        return self.name
    
```
**ClubMembership - ассоциативная сущность между пользователем и клубом**
```

class ClubMembership(models.Model):
    alpinist_id = models.ForeignKey('Alpinist', on_delete=models.CASCADE)
    club_id = models.ForeignKey('Club', on_delete=models.CASCADE)
    date_from = models.DateField(auto_now_add=True)
    date_to = models.DateField(null=True, blank=True)
    admin_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.club_id.name + ' - ' + self.alpinist_id.first_name + ' ' + self.alpinist_id.last_name

```
**Mountain**
```

class Mountain(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    hight = models.IntegerField()

    def __str__(self):
        return self.name
        
```
**Climbing**
```

class Climbing(models.Model):

    level_types = (
        ('Для всех', 'Для всех'),
        ('Для продвинутых', 'Для продвинутых'),
        ('Для профи', 'Для профи'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    max_participants = models.IntegerField(validators=[MinValueValidator(2)], default=10)
    cost = models.IntegerField(default=10000)
    start_date_plan = models.DateTimeField()
    start_date_fact = models.DateTimeField(null=True, blank=True)
    finish_date_plan = models.DateTimeField()
    finish_date_fact = models.DateTimeField(null=True, blank=True)
    level = models.CharField(max_length=15, choices=level_types)
    succeed = models.BooleanField(default=False)
    mountain_id = models.ForeignKey('Mountain', on_delete=models.CASCADE)
    club_id = models.ForeignKey('Club', on_delete=models.CASCADE)
    alpinists = models.ManyToManyField('Alpinist', through='Participating')

    def __str__(self):
        return self.name#'Восхождение на ' + self.mountain_id.name

        
```
**Participating - ассоциативная сущность между пользователем и восхождением**
</br> Поле succeed меняет сам пользователь после восхождения
```

class Participating(models.Model):
    alpinist_id = models.ForeignKey('Alpinist', on_delete=models.CASCADE)
    climbing_id = models.ForeignKey('Climbing', on_delete=models.CASCADE)
    succeed = models.BooleanField(default=False)
    admin_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.climbing_id.name + ' - ' + self.alpinist_id.first_name + ' ' + self.alpinist_id.last_name
 
```
**EmergencySituation**
```

class EmergensySituation(models.Model):
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.TextField()
    participating_id = models.ForeignKey('Participating', on_delete=models.CASCADE)

    def __str__(self):
        return self.type + ' ' + self.participating_id.alpinist_id.first_name + ' ' + self.participating_id.alpinist_id.first_name + ' ' + self.participating_id.climbing_id.mountain_id.name

    
```