# Практика

Работа с запросами в Django ORM.

=== "Модели"

    ```Python
    from django.db import models


    class CarOwner(models.Model):
        last_name = models.CharField(max_length=30)
        first_name = models.CharField(max_length=30)
        birth_date = models.DateField()
    
        def __str__(self):
            return f'{self.first_name} {self.last_name}'
    
    
    class License(models.Model):
        LICENSE_TYPE = (
            ('B', 'passenger car'),
            ('C', 'truck'),
            ('D', 'bus'),
        )
        car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
        license_number = models.IntegerField()
        type = models.CharField(max_length=2, choices=LICENSE_TYPE)
        date_of_issue = models.DateField()
    
    
    class Car(models.Model):
        license_plate_number = models.CharField(max_length=15)
        brand = models.CharField(max_length=20)
        model = models.CharField(max_length=20)
        color = models.CharField(max_length=30)
        owner = models.ManyToManyField(CarOwner, through='Ownership')
    
        def __str__(self):
            return self.license_plate_number
    
    
    class Ownership(models.Model):
        user = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
        car = models.ForeignKey(Car, on_delete=models.CASCADE)
        date_start = models.DateField()
        date_end = models.DateField(null=True, blank=True)
        ended = models.BooleanField()
    ```

=== "Задание 1"

    ```Python
    
    from django.utils import datetime
    from project_first_app.models import CarOwner, Car, Ownership, Licence
    
    owners = CarOwner.objects.bulk_create(
        [
            CarOwner(last_name="Беляев ", first_name="Глеб ", birth_date=datetime.now()),
            CarOwner(last_name="Пономарев", first_name="Егор", birth_date=datetime.now()),
            CarOwner(last_name="Сидорова", first_name="Марьяна", birth_date=datetime.now()),
            CarOwner(last_name="Гордеева", first_name="Ксения", birth_date=datetime.now()),
            CarOwner(last_name="Синицына", first_name="Екатерина", birth_date=datetime.now()),
            CarOwner(last_name="Абрамов", first_name="Фёдор", birth_date=datetime.now()),
        ]
    )
    
    cars = Car.objects.bulk_create(
        [
            Car(license_plate_number=" Х574ТМ", brand="Jeep", model="Compass", color="черный"),
            Car(license_plate_number="У342УР", brand="Honda", model="Clarity", color="синий"),
            Car(license_plate_number="С699НО", brand="Ford", model="Fusion", color="белый"),
            Car(license_plate_number="У253КМ", brand="Kia", model="Rio", color="серый"),
            Car(license_plate_number="Т191ВХ", brand="Volkswagen", model="Atlas", color="черный"),
            Car(license_plate_number="E543MK", brand="Ford", model="Maverick", color="зеленый"),
        ]
    )
    
    ownerships = Ownership.objects.bulk_create(
        [Ownership(owner=owners[i], car=cars[i], start_date=datetime.now()) for i in range(6)]
    )
    
    licences = DrivingLicence.objects.bulk_create(
        [Licence(owner=owners[i], number=str(i + 1) * 10, type="B", issue_date=datetime.now()) for i in range(6)]
    )

    ```


=== "Задание 2"

    ```Python
    from django.utils import datetime
    from project_first_app.models import CarOwner, Car, Licence
    
    
    toyota_cars = Car.objects.filter(brand="Ford").all()
    
    ivan_owners = CarOwner.objects.filter(first_name="Екатерина").all()
    
    random_owner_id = CarOwner.objects.order_by("?").values_list("id", flat=True).first()
    random_owner_licence = DrivingLicence.objects.get(owner_id=random_owner_id)
    
    black_car_owners = CarOwner.objects.filter(ownerships__car__color="черный").all()
    
    this_year_owners = CarOwner.objects.filter(licences__issue_date__year=datetime.now().year).all()

    ```

=== "Задание 3"

    ```Python

    from django.db.models import Min, Max, Count
    
    from project_first_app.models import CarOwner, Car, Ownership, Licence
    
    oldest_licence = Licence.objects.aggregate(max_issue_date=Min("issue_date"))["max_issue_date"]
    
    newest_ownership = Ownership.objects.aggregate(max_start_date=Max("start_date"))["max_start_date"]
    
    ownerships_counts = CarOwner.objects.annotate(count=Count("ownerships"))
    ownerships_counts_str = [f"{owner.full_name}: {owner.count}" for owner in ownerships_counts]
    
    cars_count_by_brands = Car.objects.values("brand").annotate(count=Count("id"))
    cars_count_by_brands_str = [f"{car['brand']}: {car['count']}" for car in cars_count_by_brands]
    
    sorted_owners = CarOwner.objects.order_by("ownerships__start_date").all()

    ```
