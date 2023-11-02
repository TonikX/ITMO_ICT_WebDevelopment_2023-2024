#Модели данных

Для работы с базой данных в Django используются модели (файл models.py).
Ниже приведены модели, нужные для моего сайта.

##Модель, которая определяет профиль пользователя: хранении информации о пользователе, включая его имя, фамилию, и связь с объектом User
    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)


##Модель конференций: содержит информацию о конференции
    class Conference(models.Model):
        name = models.CharField(max_length=255)
        topics = models.TextField()
        location = models.CharField(max_length=255)
        start_date = models.DateField()
        end_date = models.DateField()
        description = models.TextField()
        venue_description = models.TextField()
        participation_conditions = models.TextField()
    
        def __str__(self):
            return self.name

##Модель регистрации на конференцию: содержит информацию об учете регистраций пользователей на конференции 
    class Registration(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255, default='', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"Registration for {self.conference.name} by {self.user.username}"

##Модель отзывов: содержит информацию об отзыве на конференцию и ее авторе
    class Review(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])


    def __str__(self):
    return f"Review by {self.user.username} on {self.conference.name}"