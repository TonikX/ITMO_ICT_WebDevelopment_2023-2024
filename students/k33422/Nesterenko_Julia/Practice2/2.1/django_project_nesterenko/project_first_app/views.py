from django.http import Http404
from django.shortcuts import render
from .models import Owner


def owner(request, id):
    try:
        o = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Not found")
    return render(request, 'owner.html', {'owner': o})
