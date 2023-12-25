from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @staff_member_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Доступ запрещен")

    return _wrapped_view