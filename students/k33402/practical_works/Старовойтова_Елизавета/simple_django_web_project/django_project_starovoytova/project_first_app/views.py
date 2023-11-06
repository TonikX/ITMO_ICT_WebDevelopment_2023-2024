from django.shortcuts import render
from .models import Owner


def owner_detail(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)  # Получить объект владельца по его идентификатору
    return render(request, 'owner_detail.html', {'owner': owner})


