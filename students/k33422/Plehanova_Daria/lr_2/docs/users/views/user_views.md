# Контроллеры приложения Users

## UserRegisterView

**Маршрут:**  
`form_class`: CustomUserCreationForm  
**Шаблон:**  
`template_name`: users/register.html  
**URL после успешной регистрации:**  
`success_url`: login

### Описание:
`UserRegisterView` используется для регистрации новых пользователей. Он использует форму `CustomUserCreationForm` и при успешной регистрации перенаправляет пользователя на страницу входа.

## UserLoginView

**Маршрут:**  
`form_class`: CustomAuthenticationForm  
**Шаблон:**  
`template_name`: users/login.html  
**URL после успешной авторизации:**  
`success_url`: home  
**Перенаправление аутентифицированных пользователей:**  
`redirect_authenticated_user`: True

### Описание:
`UserLoginView` используется для авторизации пользователей. Он использует форму `CustomAuthenticationForm`. Если пользователь уже авторизован, он будет перенаправлен на главную страницу.

## ForbiddenView

**Шаблон:**  
`template_name`: 403.html

### Описание:
`ForbiddenView` используется для отображения страницы с ошибкой "403 Запрещено".

## NotFoundView

**Шаблон:**  
`template_name`: 404.html

### Описание:
`NotFoundView` используется для отображения страницы с ошибкой "404 Не найдено".
