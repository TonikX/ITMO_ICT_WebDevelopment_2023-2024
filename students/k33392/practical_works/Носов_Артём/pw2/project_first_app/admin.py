from django.contrib import admin

from .models import Owner, Dog, Exhibition, Participate, ExampleModel, Publisher, Book, User

admin.site.register(ExampleModel)
admin.site.register(Publisher)
admin.site.register(Owner)
admin.site.register(Dog)
admin.site.register(Exhibition)
admin.site.register(Participate)
admin.site.register(Book)
admin.site.register(User)