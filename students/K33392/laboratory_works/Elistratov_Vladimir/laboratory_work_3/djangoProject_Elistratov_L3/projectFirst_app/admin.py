from django.contrib import admin
from .models import Person, FriendShip, Vault, VaultAccess, Comments, File

# Register your models here.


class Admin(admin.ModelAdmin):
    admin.site.register(Person)
    admin.site.register(FriendShip)
    admin.site.register(Vault)
    admin.site.register(VaultAccess)
    admin.site.register(Comments)
    admin.site.register(File)