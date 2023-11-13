# Формы

Перед тем как писать представления, нам нужно создать некоторые формы. Для этого создадим файл `forms.py` в нашем приложении.

=== "Регистрация"

    ```Python
    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User


    --8<-- "laboratory_work_2/hotelProject/hotel_app/forms.py:8:22"

    ```

    Создадим класс, наследуя встроенную форму для регистрации новых пользователей `UserCreationForm`.
    Добавим поле почты.

=== "Бронирование"

    ```Python
    from django import forms
    from .models import Booking


    --8<-- "laboratory_work_2/hotelProject/hotel_app/forms.py:24:45"
    ```

    Форма для бронирования. Вместе с реквестом в нее передается информация о текущем пользователе и о комнате, 
    которую он бронирует. Юзеру нужно только ввести информацию о дате заселения и выселения.

=== "Отзыв"

    ```Python
    from django import forms
    from .models import Comment


    --8<-- "laboratory_work_2/hotelProject/hotel_app/forms.py:46:65"
    ```

    Самая базовая форма, основанная на модели. Нам требуются только 2 поля: текст отзыва и рейтинг.