from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class BaseCurrentUserOrAdmin(IsAuthenticated):
	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		
		return request.user.is_staff


class CurrentUserOrAdminForProfiles(BaseCurrentUserOrAdmin):
	def has_object_permission(self, request, view, obj):
		if super().has_object_permission(request, view, obj):
			return True
		
		if hasattr(obj, 'user'):
			return obj.user == request.user
		
		return False


class CurrentUserOrAdminForGroupMember(BaseCurrentUserOrAdmin):
	def has_permission(self, request, view):
		if not super().has_permission(request, view):
			return False
		
		if view.action in ['create', 'update', 'partial_update', 'destroy']:
			is_alpinist = hasattr(request.user, 'alpinist_profile') and request.user.alpinist_profile is not None
			return is_alpinist or request.user.is_staff
		
		return True
	
	def has_object_permission(self, request, view, obj):
		if super().has_object_permission(request, view, obj):
			return True
		
		if hasattr(obj, 'alpinist'):
			return obj.alpinist.user == request.user
		
		return False


class IsAdminOrReadOnly(IsAuthenticated):
	def has_permission(self, request, view):
		if request.method in SAFE_METHODS:
			return True
		
		return request.user.is_staff


class BaseIsGuideOrAdmin(BaseCurrentUserOrAdmin):
	def has_permission(self, request, view):
		if not super().has_permission(request, view):
			return False
		
		if view.action in ['create', 'update', 'partial_update', 'destroy']:
			is_guide = hasattr(request.user, 'guide_profile') and request.user.guide_profile is not None
			return is_guide or request.user.is_staff
		
		return True


class IsGuideOrAdminForClimb(BaseIsGuideOrAdmin):
	def has_object_permission(self, request, view, obj):
		if super().has_object_permission(request, view, obj):
			return True
		
		if hasattr(obj, 'guide'):
			return obj.guide.user == request.user
		
		return False


class IsGuideOrAdminForGroup(BaseIsGuideOrAdmin):
	def has_object_permission(self, request, view, obj):
		if super().has_object_permission(request, view, obj):
			return True
		
		if hasattr(obj, 'climb'):
			return obj.climb.guide.user == request.user
		
		return False
