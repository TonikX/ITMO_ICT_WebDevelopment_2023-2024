from project_firts_app.models import CarOwner

new_car_owner = CarOwner.objects.create(surname="Koligny", first_name="Gaspard")
print('success')
