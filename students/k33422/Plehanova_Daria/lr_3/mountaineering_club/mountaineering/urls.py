from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AlpinistViewSet, GuideViewSet

router = DefaultRouter()
router.register(r'alpinists', AlpinistViewSet)
router.register(r'guides', GuideViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
