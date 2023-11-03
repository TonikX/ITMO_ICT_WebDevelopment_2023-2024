from django.apps import apps
from django.contrib import admin

app = apps.get_app_config("project_first_app")

for model_name, model in app.models.items():
    admin.site.register(model)
