Тут я опишу, что и как я устанавливала для бэкэнд и фронтэнд-части лабораторной работы:

Шаг 1: Определяем зависимости для проекта и делаем нужные pip(Django)

![img_1.png](..%2Fimg%2Flw4%2Fimg_1.png)
![img_2.png](..%2Fimg%2Flw4%2Fimg_2.png)
![img_3.png](..%2Fimg%2Flw4%2Fimg_3.png)

Добавим в urls.py в urlpatterns: 
            urlpatterns = [ … 
            path('api/v1/',include('djoser.urls')), 
            path('api/v1/',include('djoser.urls')), 
            ] 

Далее поднастроим CORS: 
    CORS_ALLOWED_ORIGINS = [ "http://localhost:8080", ] 
    MIDDLEWARE = [ 'django.middleware.security.SecurityMiddleware', 'django.contrib.sessions.middleware.SessionMiddleware', 'corsheaders.middleware.CorsMiddleware', … ]

![img_4.png](..%2Fimg%2Flw4%2Fimg_4.png)
![img_5.png](..%2Fimg%2Flw4%2Fimg_5.png)

Организация проверки работы сервера:
![img_6.png](..%2Fimg%2Flw4%2Fimg_6.png)

Установка для работы с Vue.js:
![img_8.png](..%2Fimg%2Flw4%2Fimg_8.png)
![img_9.png](..%2Fimg%2Flw4%2Fimg_9.png)

Проверим, что всё работает и запускается на фронтэнде:

![img_7.png](..%2Fimg%2Flw4%2Fimg_7.png)