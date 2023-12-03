from django.urls import include, path

from mountaineering.urls import urlpatterns as mountaineering_urls

urlpatterns = [
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.authtoken'))
]

urlpatterns += mountaineering_urls
