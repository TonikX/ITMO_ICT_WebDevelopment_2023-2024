from practice.models import Car, CarOwner, DriverLicence, Ownership
from django.db.models import Max, Count

# Самая старая лицензия
# oldest_licence = DriverLicence.objects.aggregate(oldest=Max("recieved_date"))
# print(oldest_licence)

# Самое новое приобретение
# ownership = Ownership.objects.aggregate(Max("start_date"))
# print(ownership)

# Количество машин во владении каждого владельца
# car_owners = CarOwner.objects.annotate(cnt=Count('ownership'))
# print([f"Количество машин во владении {i.name} {i.surname} составляет {i.cnt}" for i in car_owners])

# Количество по брендам
# car_dict = Car.objects.values("brand").annotate(cnt=Count("id"))
# print([f"Количество машин {i['brand']} составляет {i['cnt']}" for i in car_dict])

sort_owners = DriverLicence.objects.order_by("recieved_date").all()
print([f"Владелец {i.id} получил лицензию {i.recieved_date}" for i in sort_owners])
# print(result)