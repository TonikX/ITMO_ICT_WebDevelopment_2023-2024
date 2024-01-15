from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default='avatar.svg')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
     
class BaseModel(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # TODO: automatic creator setting

    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name    
    
class Skill(BaseModel):
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name

class UserSkills(BaseModel):
    skills = models.ManyToManyField('Skill', verbose_name='Навыки', related_name='user_skills')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class File(BaseModel):
    file_field = models.FileField(upload_to="users-files")

class ProjectTopic(BaseModel):
    description = models.TextField(null=True)

class Project(BaseModel):
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    topics = models.ManyToManyField('ProjectTopic', verbose_name='Темы', related_name='project_topics')

class GradeReport(BaseModel):
    projects = models.ManyToManyField('Project', verbose_name='Проекты', related_name='gradereport_projects')

class ProjectOfUser(BaseModel):
	project_field = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
	user_field = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Teacher(BaseModel):
	user_field = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Student(BaseModel): 
	user_field = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Grade(BaseModel):
	student_field = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
	project_field = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
	grade_field = models.SmallIntegerField()

class ProjectMeeting(BaseModel):
	project_field = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

class Meeting(BaseModel):
	users_one_field = models.ManyToManyField('User', verbose_name='Люди', related_name='meeting_users')
      