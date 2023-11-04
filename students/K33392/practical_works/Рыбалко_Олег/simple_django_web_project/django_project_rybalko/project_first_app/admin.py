from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

app = apps.get_app_config("project_first_app")

for model_name, model in app.models.items():
    if model_name == "carowner":
        admin.site.register(model, UserAdmin)
    else:
        admin.site.register(model)
