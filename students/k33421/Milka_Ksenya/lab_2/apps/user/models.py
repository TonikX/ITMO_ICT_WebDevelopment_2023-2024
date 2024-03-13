from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.user.managers import UserManager


class Roles:
    STUDENT = 'student'
    TEACHER = 'teacher'

    @classmethod
    def get_role_names(cls):
        return (
            cls.STUDENT,
            cls.TEACHER,
        )


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('date_of_birth',)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    @property
    def role(self):
        for role in Roles.get_role_names():
            if hasattr(self, role):
                return role
        return None

    def __str__(self):
        return f"{self.role} {self.full_name}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
