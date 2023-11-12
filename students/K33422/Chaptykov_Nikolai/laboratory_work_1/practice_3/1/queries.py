from practice.models import Car, CarOwner, DriverLicence, Ownership
# Все ВАЗы
# print(Car.objects.filter(brand="ВАЗ"))

# Все водители Симеоны
# print(CarOwner.objects.filter(name="Симеон"))

# Лицензия по водителю
# owner = getattr(CarOwner.objects.first(), 'id')
# print(DriverLicence.objects.filter(owner_id=owner))

# хозяева баклажановых машин
# ownership = Ownership.objects.filter(car_id__color="Баклажановый")
# print([CarOwner.objects.get(id=i['owner_id']) for i in ownership.values("owner_id")])

# владеющие авто с 2010
import datetime

datetime_str = "12.11.2023"
datetime_object = datetime.date(2023, 10, 12)

ownership = Ownership.objects.filter(start_date__gte=datetime_object)
print(ownership)

# запускать через exec("")