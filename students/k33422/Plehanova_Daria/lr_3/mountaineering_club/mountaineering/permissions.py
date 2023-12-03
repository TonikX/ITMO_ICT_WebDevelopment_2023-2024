from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class CurrentUserOrAdmin(IsAuthenticated):
	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		
		user = request.user
		return user.is_staff or obj.user.pk == user.pk
