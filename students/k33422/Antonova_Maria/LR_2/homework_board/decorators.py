from django.contrib.auth.decorators import user_passes_test # для проверки пользовательских условий

def staff_required(function=None, redirect_field_name=None, login_url=None): #
    actual_decorator = user_passes_test( # проверяет, является ли пользователь сотрудником
        lambda u: u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name #будет использоваться для перенаправления
    )
    if function:
        return actual_decorator(function)
    return actual_decorator # только пользователи с правами администратора или персоналом имели доступ к этим представлениям. Он выполняет проверку, является ли текущий пользователь сотрудником, и если нет, перенаправляет его
