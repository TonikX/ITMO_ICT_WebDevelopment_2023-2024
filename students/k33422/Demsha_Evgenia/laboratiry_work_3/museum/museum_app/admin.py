from django.contrib import admin
from .models import Museum, Author, Card, Item, Foundation, Exhibition, ItemToExhibition, CardToFoundation
# Register your models here.

admin.site.register(Museum)
admin.site.register(Author)
admin.site.register(Card)
admin.site.register(Item)
admin.site.register(Foundation)
admin.site.register(Exhibition)
admin.site.register(ItemToExhibition)
admin.site.register(CardToFoundation)
