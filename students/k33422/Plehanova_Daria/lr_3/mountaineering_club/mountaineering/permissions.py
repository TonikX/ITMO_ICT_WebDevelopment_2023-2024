from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class CurrentUserOrAdmin(IsAuthenticated):
	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		
		user = request.user
		return user.is_staff or obj.user == user


class IsAdminOrReadOnly(IsAuthenticated):
	def has_permission(self, request, view):
		if request.method in SAFE_METHODS:
			return True
		
		user = request.user
		return user.is_staff


class BaseIsGuideOrAdmin(IsAuthenticated):
	def has_permission(self, request, view):
		if not super().has_permission(request, view):
			return False
		
		if view.action in ['create', 'update', 'partial_update', 'destroy']:
			is_guide = hasattr(request.user, 'guide_profile') and request.user.guide_profile is not None
			return is_guide or request.user.is_staff
		
		return True
	
	def has_object_permission(self, request, view, obj):
		return request.method in SAFE_METHODS


class IsGuideOrAdminForClimb(BaseIsGuideOrAdmin):
	def has_object_permission(self, request, view, obj):
		if super().has_object_permission(request, view, obj):
			return True
		
		if hasattr(obj, 'guide'):
			return obj.guide.user == request.user or request.user.is_staff
		
		return False


class IsGuideOrAdminForGroup(BaseIsGuideOrAdmin):
	def has_object_permission(self, request, view, obj):
		if super().has_object_permission(request, view, obj):
			return True
		
		if hasattr(obj, 'climb'):
			return obj.climb.guide.user == request.user or request.user.is_staff
		
		return False
