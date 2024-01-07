from django.db import models


class Zoo(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=500)
    area = models.ForeignKey('system.Area', related_name='buildings', on_delete=models.CASCADE,
                            null=True, blank=True)

    def __str__(self):
        return self.name

class Aviary(models.Model):
    name = models.CharField(max_length=500)
    building = models.ForeignKey('system.Building', related_name='aviaries', on_delete=models.CASCADE,
                            null=True, blank=True)
    
    communal = models.BooleanField()
    winter_place = models.BooleanField(default=False)
    additional = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

class TypeOfDiet(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Diet(models.Model):
    num = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=500)
    type = models.ForeignKey('system.TypeOfDiet', related_name='diets', on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        return self.name


class Habitat(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    characteristic = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class WinterPlace(models.Model):
    code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=500)
    date_to = models.DateField()
    date_from = models.DateField()

    def __str__(self):
        return self.name

class Animal(models.Model):
    num = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.TextField(max_length=2, choices=(('m', 'm'), ('f', 'f')))
    birthdate = models.DateField()
    diet = models.ForeignKey('system.Diet', related_name='animals_on_this_diet', on_delete=models.CASCADE,
                             null=True, blank=True)

    winter_place = models.ForeignKey('system.WinterPlace', related_name='birds_wintering', on_delete=models.CASCADE,
                                     null=True, blank=True)

    winter_sleeping = models.IntegerField(null=True, blank=True)
    normal_temperature = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Owning(models.Model):
    animal = models.OneToOneField('system.Animal', related_name='owning', on_delete=models.CASCADE,
                                  null=True, blank=True)

    in_lease = models.BooleanField()

    owner = models.ForeignKey('system.Zoo', related_name='owned_animals', on_delete=models.CASCADE,
                              null=True, blank=True)

    here_now = models.ForeignKey('system.Zoo', related_name='animals_here', on_delete=models.CASCADE,
                                 null=True, blank=True)

    since = models.DateField()
    cost = models.FloatField()

    def __str__(self):
        return f"{self.animal} owned by {self.owner}"

class AnimalInAviary(models.Model):
    animal = models.OneToOneField('system.Animal', related_name='where', on_delete=models.CASCADE,
                                  null=True, blank=True)
    aviary = models.ForeignKey('system.Aviary', related_name='who', on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return f"{self.animal} in {self.aviary}"


class Worker(models.Model):
    num = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=500)
    birthday = models.DateField()
    animals = models.ManyToManyField('system.Animal', related_name='wathers')
    type = models.TextField(max_length=20, choices=(('V', 'V'), ('W', "W")))

    def __str__(self):
        return self.name



