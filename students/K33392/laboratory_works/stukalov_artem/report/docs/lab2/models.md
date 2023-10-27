# Модели

В рамках проекта можмно выделить 4 основных модели:

- User
- Flight
- Ticket

## User

Замена дефолтной модели пользователя с добавлением дополнительных полей:

- first_name
- last_name
- passport
- date_of_birth

## Flight

Модель представлябщая собой рейс. Хранит следющую информацию:

- Город вылета/прилета
- Время вылета
- Номер гейта
- Уникальное имя рейса
- Авикомпания
- Модель самолета

## Ticket

Куаленный пользователем билет на рейс. Хранит следющую информацию:

- Номер рейса
- Место в самолете
- Пассажир

=== "User"

    ```Python title="User"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:5:12"
    ```

=== "AirLine"

    ```Python title="AirLine"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:15:19"
    ```

=== "City"

    ```Python title="City"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:22:26"
    ```

=== "PlaneModel"

    ```Python title="PlaneModel"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:29:35"
    ```

=== "Flight"

    ```Python title="Flight"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:38:54"
    ```

=== "Ticket"

    ```Python title="Ticket"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:57:64"
    ```

=== "Comment"

    ```Python title="Comment"
    --8<-- "laboratory_work_2/air_tickets_booking/models.py:67:72"
    ```
