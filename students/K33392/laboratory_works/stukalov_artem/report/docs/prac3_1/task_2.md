# Задание 2

???+ question "Задание"

    - Где это необходимо, добавьте related_name к полям модели
    - Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
    - Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
    - Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
    - Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
    - Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

## Выполнение

Дополним модели `Ownership` и `DriverLicense` полями `related_name`

=== "Ownership"

    ```Python title="Ownership"
    class Ownership(models.Model):
    car = models.ForeignKey(
        "Car", null=True, on_delete=models.CASCADE, related_name="ownership"
    )
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="ownership",
    )
    start = models.DateField()
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.car.number} {self.driver.first_name}"
    ```

=== "DriverLicense"

    ```Python title="DriverLicense"
    class DriverLicense(models.Model):
    driver = models.ForeignKey(
        "Driver", on_delete=models.CASCADE, related_name="license"
    )
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    creation_date = models.DateField()

    def __str__(self):
        return f"{self.number} {self.driver.first_name}"
    ```

### Query 1

Выберем машины имеющие бренд "Brand_2"

```bash
>>> Car.objects.filter(brand="Brand_2")
<QuerySet [<Car: Number_2 Brand_2 Model_2>]>
```

### Query 2

Выберем водителей с именем "Driver_first_name_3"

```bash
>>> Driver.objects.filter(first_name="Driver_first_name_3")
<QuerySet [<Driver: Driver_first_name_3 Driver_last_name_3>]>
```

### Query 3

Найдем лицензию водителя с именем Driver_first_name_3

```bash
>>> DriverLicense.objects.filter(driver__first_name="Driver_first_name_3")
<QuerySet [<DriverLicense: NUMBER_3 Driver_first_name_3>]>
```

### Query 4

Найдем всех владельцев белых машин

```bash
>>> Car.objects.filter(color="White")
<QuerySet [<Car: Number_0 Brand_0 Model_0>, <Car: Number_1 Brand_1 Model_1>, <Car: Number_2 Brand_2 Model_2>, <Car: Number_3 Brand_3 Model_3>, <Car: Number_4 Brand_4 Model_4>]>
```

### Query 5

Найдем всех владельцев, чей год владения машиной начинается с 2023 года

```bash
>>> Driver.objects.filter(ownership__start__year__gte=2023)
<QuerySet [<Driver: Driver_first_name_0 Driver_last_name_0>, <Driver: Driver_first_name_1 Driver_last_name_1>, <Driver: Driver_first_name_2 Driver_last_name_2>, <Driver: Driver_first_name_3 Driver_last_name_3>, <Driver: Driver_first_name_4 Driver_last_name_4>]>
```
