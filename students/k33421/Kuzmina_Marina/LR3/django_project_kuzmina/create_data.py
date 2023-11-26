from django.utils import timezone
from project_first_app.models import Driver, DriverLicence, Car, Ownership

drivers_data = [
    {"username": "driver111", "last_name": "Russell", "first_name": "George", "date_of_birth": timezone.now()},
    {"username": "driver222", "last_name": "Rodríguez", "first_name": "Ricardo", "date_of_birth": timezone.now()},
    {"username": "driver333", "last_name": "Sainz", "first_name": "Carlos", "date_of_birth": timezone.now()},
    {"username": "driver444", "last_name": "Hamilton", "first_name": "Lewis", "date_of_birth": timezone.now()},
    {"username": "driver555", "last_name": "Marko", "first_name": "Helmut", "date_of_birth": timezone.now()},
    {"username": "driver666", "last_name": "Leclerc", "first_name": "Charles", "date_of_birth": timezone.now()},
]

created_drivers = []

for data in drivers_data:
    driver = Driver.objects.create_user(**data)
    created_drivers.append(driver)
    print(f"Создан водитель: {driver.username}")

# Создаем автомобили
cars_data = [
    {"number": "YCE518", "brand": "BMW", "car_model": "7 Series", "color": "Black"},
    {"number": "UGH672", "brand": "Janguar", "car_model": "XJ", "color": "Blue"},
    {"number": "BCR629", "brand": "Skoda", "car_model": "Felicia", "color": "Pink"},
    {"number": "MNB576", "brand": "Alfa Romeo", "car_model": "Giulia", "color": "Black"},
    {"number": "NLI910", "brand": "Audi", "car_model": "R8", "color": "Yellow"},
]

created_cars = []

for data in cars_data:
    car = Car.objects.create(**data)
    created_cars.append(car)
    print(f"Создан автомобиль: {car.number}")

# Создаем водительские удостоверения
licences_data = [
    {"owner": driver, "number": str(i + 1), "licence_type": chr(ord("A") + i), "date_of_release": timezone.now()}
    for i, driver in enumerate(created_drivers)
]

for data in licences_data:
    DriverLicence.objects.create(**data)

# Создаем владение
ownership_data = [
    {"driver": driver, "car": car, "date_beginning": timezone.now(), "date_end": timezone.now()}
    for driver, car in zip(created_drivers, created_cars)
]

for data in ownership_data:
    Ownership.objects.create(**data)

print("Скрипт успешно завершен.")

