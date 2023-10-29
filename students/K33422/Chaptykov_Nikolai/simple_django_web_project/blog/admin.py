from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from blog.models import Person, DriverLicense, Car, OwnerShip, CarsAndPerson, ExampleModel, Publisher, Book, PersonAdvanced, Post


class PersonInLine(admin.StackedInline):
	model = Person
	verbose_name_plural = 'Personas'
	can_delete = False

class CustomizedUserAdmin(UserAdmin):
	inlines = (PersonInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

admin.site.register(Person)
admin.site.register(PersonAdvanced)
admin.site.register(DriverLicense)
admin.site.register(Car)
admin.site.register(OwnerShip)
admin.site.register(CarsAndPerson)
admin.site.register(ExampleModel)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Post)