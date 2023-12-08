# Практическая 3.1

models.py 
```python
from django.db import models


class CarOwner(models.Model):
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Car(models.Model):
    plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.brand} {self.model} {self.plate} {self.color}"

class Ownership(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.owner} с {self.start_date} до {self.end_date}"


class DriverLicence(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    licence_id = models.CharField(max_length=10)
    licence_type = models.CharField(max_length=10)
    recieved_date = models.DateField()

    def __str__(self):
        return f"{self.owner_id} {self.licence_id}"
```
Запросы и результаты их вывода:
* Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)

![ ](/Users/aliabuskina/cars/1.png)
* Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)

![ ](/Users/aliabuskina/cars/2.png)
* Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)

![ ](/Users/aliabuskina/cars/3.png)
* Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)

![ ](/Users/aliabuskina/cars/4.png)
* Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

![ ](/Users/aliabuskina/cars/5.png)

* Вывод даты выдачи самого старшего водительского удостоверения
* 
![ ](/Users/aliabuskina/cars/6.png)
* Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе

![ ](/Users/aliabuskina/cars/7.png)
* Выведите количество машин для каждого водителя

![ ](/Users/aliabuskina/cars/8.png)
* Подсчитайте количество машин каждой марки

![ ](/Users/aliabuskina/cars/9.png)
* Отсортируйте всех автовладельцев по дате выдачи удостоверения 

![ ](/Users/aliabuskina/cars/10.png)