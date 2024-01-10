# Настройки приложения/сервера


В дефолтные параметры, определяемые в settings.py, внесены два изменения:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'rest_framework_simplejwt',
    "corsheaders",
    #

    'system.apps.SystemConfig'
]
```

для того, что бы подключть приложение. И:

```
AUTH_PROFILE_MODULE = 'system.CustomUser'
AUTH_USER_MODEL = 'system.CustomUser'
```
для переопределения пмодели юзера.

Так же добавим параметры для настрйоки jwt-аутентификации

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}
```


Так же добавим новый корень для юрл-адресов нового приложения и сваггера

```

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/', include('system.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



```