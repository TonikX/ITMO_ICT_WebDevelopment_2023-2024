# Компоненты

=== "Авторизация"

    Авторизация реализована с помощью ajax

    ```html title="Login.vue"

    --8<-- "laboratory_work_4/vue_museum/src/components/Login.vue"

    ```

=== "Список фондов"

    Обращаясь к локально запущенному серверу с django rest api по адресу 'foundations/list' получим 
    список всех фондов, а 'foundations/ratio/' вернет процентное соотношение для каждого фонда. Нажав на имя фонда, 
    перейдем к компоненту со списком карточек в фонде.

    ```html title="FoundationList.vue"

    --8<-- "laboratory_work_4/vue_museum/src/components/FoundationList.vue"

    ```

=== "Карточки в фонде"

    Карточки для конкретного фонда берутся из запроса 'foundations/<int:pk>/cards'. Кнопка "создать карточку" 
    отправит к компоненту для создания карточки. Нажав на имя карточки, перейдем к списку предметов в карточке.

    ```html title="CardList.vue"

    --8<-- "laboratory_work_4/vue_museum/src/components/CardList.vue"
    ```

=== "Добавление карточки"
    
    Здесь выполняется post-запрос на адрес 'cards/create/', а также создается объект в таблице CardToFoundtion 
    ccылающийся на только что созданную карточку и на фонд, на странице которого мы находимся.

    ```html title="CardCreate.vue"

    --8<-- "laboratory_work_4/vue_museum/src/components/CardCreate.vue"
    ```

=== "Предметы в карточке"

    По ссылке 'cards/<int:card_id>/items/' возьмем предметы, относящиеся к текущей карточке. Также добавим 
    возможность отправлять предметы на выставку: список выставок берем из 'exhibitions/list' и выполняем 
    post-pапрос на 'item-to-exhibition/'

    ```html title="CardDetail.vue"

    --8<-- "laboratory_work_4/vue_museum/src/components/CardDetail.vue"
    ```

=== "Добавление предмета"

    Здесь выполняется post-запрос на адрес 'items/create/'

    ```html title="ItemCreate.vue"

    --8<-- "laboratory_work_4/vue_museum/src/components/ItemCreate.vue"
    ```

