from practice.models import Car, CarOwner, DriverLicence, Ownership
# Все ВАЗы
# print(Car.objects.filter(brand="ВАЗ"))

# Все водители Симеоны
# print(CarOwner.objects.filter(name="Симеон"))

# Лицензия по водителю
# owner = getattr(CarOwner.objects.first(), 'id')
# print(DriverLicence.objects.filter(owner_id=owner))

# хозяева баклажановых машин
eggplant = Ownership.objects.filter(car_id__color="Баклажановый").values("owner_id__name", "owner_id__surname")
print(eggplant)

# владеющие авто с 2010
import datetime

datetime_object = datetime.date(2010, 10, 12)

ownership = Ownership.objects.filter(start_date__gte=datetime_object)
print(ownership)

# запускать через exec("")