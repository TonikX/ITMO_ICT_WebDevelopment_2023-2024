from project_first_app.models import *

toyota_cars = car.objects.filter(brand="Toyota")
for toyota_car in toyota_cars:
    print(toyota_car.state_number, toyota_car.brand, toyota_car.model, toyota_car.color)

owners_with_specific_name = carOwner.objects.filter(name="John")
for owner in owners_with_specific_name:
    print(owner.username, owner.name, owner.surname, owner.date_Birth, owner.passport, owner.address, owner.nationality)

random_user = carOwner.objects.get(id=1)

# Query the driver's license for the random user
driver_license = driver_license.objects.get(id_owner=random_user)

# Print information about the random user and their driver's license
print(f"User: {random_user.username} - {random_user.name} {random_user.surname}")
print(f"Driver's License: {driver_license.id_number} - Type: {driver_license.type} - Date of Issue: {driver_license.date_issue}")

red_cars = car.objects.filter(color="Red")
for red_car in red_cars:
    print(red_car.state_number, red_car.brand, red_car.model, red_car.color)
