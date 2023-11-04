from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser
from django.db.models import Model

app = apps.get_app_config("project_first_app")

for model_name, model in app.models.items():
    if issubclass(model, Model):
        admin.site.register(model)
    elif issubclass(model, AbstractUser):
        admin.site.register(model, UserAdmin)
