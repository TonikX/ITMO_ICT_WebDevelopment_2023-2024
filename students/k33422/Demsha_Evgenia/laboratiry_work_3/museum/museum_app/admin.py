from django.contrib import admin
from .models import Museum, Author, Set, Item, Foundation, Exhibition, ItemToExhibition, SetToFoundation
# Register your models here.

admin.site.register(Museum)
admin.site.register(Author)
admin.site.register(Set)
admin.site.register(Item)
admin.site.register(Foundation)
admin.site.register(Exhibition)
admin.site.register(ItemToExhibition)
admin.site.register(SetToFoundation)
