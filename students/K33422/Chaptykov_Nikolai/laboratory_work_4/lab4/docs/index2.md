# Практическая 4.3
## Особенности выполнения работы
Настройка CORS в среде Django не является задачей сложной, однако стоит обращать внимание на порядок элементов в списке MIDDLEWARE из файла settings.py. Также в список установленных приложений необходимо добавить элемент 'corsheaders'
## Список MIDDLEWARE
```Python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
```