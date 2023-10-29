from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from hotel_app.models import Hotel, Room, Booking, Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView




