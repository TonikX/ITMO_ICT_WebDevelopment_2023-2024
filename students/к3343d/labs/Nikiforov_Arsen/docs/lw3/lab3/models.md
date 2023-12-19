# Описание моделей Django

## CustomUser

`CustomUser` расширяет стандартную модель пользователя Django (`AbstractUser`), добавляя новое поле `phone` для хранения телефонного номера пользователя.

```python
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
```
- `AbstractUser` включает стандартные поля, такие как имя пользователя, email, пароль.
- `phone`: Необязательное поле для хранения номера телефона, `max_length=15` означает, что номер телефона не может быть длиннее 15 символов.


## Floor

`Floor` представляет этаж в здании отеля. Имеет одно поле `number`, которое указывает номер этажа.

```python
class Floor(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f"Floor {self.number}"
```
- `number`: Целочисленное поле для хранения номера этажа.
- Метод `__str__`: Возвращает строку "Floor {number}", которая используется для отображения объекта этажа в административном интерфейсе Django.


## Room

`Room` описывает комнату в отеле. Содержит информацию о типе комнаты, стоимости, этаже и статусе.

```python
class Room(models.Model):
    # Варианты типов комнат
    ROOM_TYPES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    )
    # Варианты статусов комнаты
    ROOM_STATUSES = (
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('cleaning', 'Cleaning'),
    )
    room_type = models.CharField(max_length=100, choices=ROOM_TYPES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    status = models.CharField(max_length=100, choices=ROOM_STATUSES)

    def __str__(self):
        return f"{self.get_room_type_display()} on Floor {self.floor.number}"
```
- `room_type`: Тип комнаты с определенными вариантами.
- `cost`: Десятичное поле для стоимости комнаты.
- `floor`: Внешний ключ на модель `Floor`, показывает, к какому этажу относится комната.
- `status`: Статус комнаты (доступна, занята, уборка).


## ClientInfo, Client, Employee, Day, EmployeeFloor, EmployeeDay

Эти модели представляют различные аспекты системы управления отелем.

- `ClientInfo`: Содержит информацию о клиенте, включая номер паспорта, имя, фамилию, отчество, город и дату заезда.
- `Client`: Связывает клиента (`ClientInfo`) с комнатой (`Room`).
- `Employee`: Описывает сотрудника отеля.
- `Day`: Представляет день недели.
- `EmployeeFloor`: Указывает, какие сотрудники работают на каких этажах.
- `EmployeeDay`: Указывает, какие сотрудники работают в какие дни.


```python
class ClientInfo(models.Model):
    passport_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    check_in_date = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Client(models.Model):
    client_info = models.ForeignKey(ClientInfo, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='clients')

    def __str__(self):
        return f"Client {self.client_info.first_name} {self.client_info.last_name}"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Day(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EmployeeFloor(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} on Floor {self.floor.number}"

class EmployeeDay(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} on {self.day.name}"

```
- В каждой модели используется метод `__str__` для возвращения удобочитаемого представления объекта.
- В моделях `Client`, `EmployeeFloor`, `EmployeeDay` используются внешние ключи для связи с другими моделями.
