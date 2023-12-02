from project_first_app.models import *

toyota_cars = Car.objects.filter(model="Toyota")

for car in toyota_cars:
  print(f"Car Number: {car.number}")
  print(f"Model: {car.model}")
  print(f"Color: {car.color}")
  print("--------------------")


alice_drivers = CarOwner.objects.filter(first_name="Alice")
for driver in alice_drivers:
  print(f"Driver Name: {driver.first_name}")
  print(f"Date of Birth: {driver.date_of_birth}")
  print("--------------------")

driver = CarOwner.objects.get(first_name="Jane")

print(f"Driver Name: {driver.first_name}")
print(f"Date of Birth: {driver.date_of_birth}")
print("--------------------")

driver_licenses = DriversLicence.objects.filter(owner=driver)
for license in driver_licenses:
  print(f"License Number: {license.number}")
  print(f"License Type: {license._type}")
  print(f"Issue Date: {license.issue_date}")
  print("--------------------")

# Query all car owners with red cars
red_cars = Car.objects.filter(color="Red")
for car in red_cars:
  print(f"Car Number: {car.number}")
  print(f"Model: {car.model}")
  print(f"Color: {car.color}")
  print("--------------------")

target_year = 2023
owners_with_cars_from_year = CarOwner.objects.filter(
    ownership__start_date__year=target_year
).distinct()

for owner in owners_with_cars_from_year:
  print(f"Owner Name: {owner.first_name}")
  print(f"Date of Birth: {owner.date_of_birth}")
  print("--------------------")