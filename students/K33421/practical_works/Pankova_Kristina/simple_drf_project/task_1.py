from datetime import datetime

# add licence to each owner
for i, owner in enumerate(CarOwner.objects.all())[6:7]:
    license = DriversLicence(owner_car=owner, licence_number=f"0877{i}939", type="Valid", given_at="2023-07-25")
    license.save()
    new_car = Car(gov_number=f"27232{i}", car_make=f"121232{i}", model="car_model", color="pink")
    new_car.save()
    car_ownership = CarOwnership(car=new_car, owner=owner, date_begin=datetime.today().strftime('%Y-%m-%d'))
    car_ownership.save()





