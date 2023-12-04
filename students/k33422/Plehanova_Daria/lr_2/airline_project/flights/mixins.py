from django.core.exceptions import PermissionDenied


class UserReviewMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("Вы не имеете права на это действие.")
        return obj
