from django.contrib import admin
from .models import Newspaper, PrintingHouse, PostOffice, NewspaperPrint, NewspaperArrival, NewspaperOrder, UserProfile

@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'edition_index', 'editor_last_name', 'editor_first_name', 'editor_middle_name', 'price']

@admin.register(PrintingHouse)
class PrintingHouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'is_closed']

@admin.register(PostOffice)
class PostOfficeAdmin(admin.ModelAdmin):
    list_display = ['number', 'address']

@admin.register(NewspaperPrint)
class NewspaperPrintAdmin(admin.ModelAdmin):
    list_display = ['newspaper', 'printing_house', 'circulation']

@admin.register(NewspaperArrival)
class NewspaperArrivalAdmin(admin.ModelAdmin):
    list_display = ['newspaper', 'post_office', 'quantity']

@admin.register(NewspaperOrder)
class NewspaperOrderAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'newspaper', 'quantity', 'order_date']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_postoffice_number']
