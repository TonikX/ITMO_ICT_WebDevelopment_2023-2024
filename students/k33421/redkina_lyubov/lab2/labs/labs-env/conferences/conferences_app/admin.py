from django.contrib import admin
from .models import Author, Conference, Registration, Review, Presentation


class PresentationAdmin(admin.ModelAdmin):
    list_display = ("conference", "author", "title", "approved_pres")

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin or (obj and obj.author == request.user and not obj.approved):
            return True
        return False


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("author", "conference", "title", "approved_reg")

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "occupation", "is_admin")


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Conference)
admin.site.register(Review)
