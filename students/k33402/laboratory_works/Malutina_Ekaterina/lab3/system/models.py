from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


# модель менеджера
class CustomUserManager(BaseUserManager):
    # создание пользователя
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    # создание админа
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


# модель пользователя
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

    id = models.BigAutoField(primary_key=True)

    norm_cal = models.FloatField(default=0.0, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    linkedin_token = models.TextField(blank=True, default='')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    avatar = models.ImageField(default='default.png')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


# модель продукта
class Product(models.Model):
    name = models.CharField(max_length=200)
    calories = models.FloatField()


# модель даты
class Day(models.Model):
    date = models.DateField()


# модель съеденного
class Eaten(models.Model):
    product = models.ForeignKey(Product, related_name='what_eaten', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='who_eat', on_delete=models.CASCADE)
    when_date = models.ForeignKey(Day, related_name='eaten', on_delete=models.CASCADE)
    when_time = models.TimeField()
