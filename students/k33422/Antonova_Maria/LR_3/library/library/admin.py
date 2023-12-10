from django.contrib import admin
from .models import Book, Room, Reader, User, BookInstance

admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Room)
admin.site.register(User)
admin.site.register(BookInstance)
