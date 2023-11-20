# C:\WEBDJANGO\myproject\myapp\admin.py
from django.contrib import admin
from .models import Tour, Reservation, Review

admin.site.register(Tour)
admin.site.register(Reservation)
admin.site.register(Review)

