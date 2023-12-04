from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

User = get_user_model()


class BaseProfilesViewSet(viewsets.ModelViewSet):
	"""
	Базовый набор представлений для моделей c типом связи один к одному с пользователем.
	"""
	
	def perform_create(self, serializer):
		user_id = self.request.data.get('user_id')
		current_user = self.request.user
		
		if user_id and current_user.is_staff:
			user = get_object_or_404(User, id=user_id)
		else:
			user = current_user
		
		serializer.save(user=user)
