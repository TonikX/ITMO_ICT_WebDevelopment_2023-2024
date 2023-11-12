from practice.models import Car, CarOwner, DriverLicence, Ownership
from django.db.models import Max, Count


# ownership = Ownership.objects.aggregate(Max("start_date"))
# print(ownership)

# owners = CarOwner.objects.all()
# ownership = [Ownership.objects.filter(owner_id=i).values().aggregate(Count("id")) for i in owners]
# print(ownership)

# cars = Car.objects.values("brand").distinct()
# print([Car.objects.filter(brand=i['brand']).values("brand").annotate(brand_cnt=Count("id")) for i in cars])

# owners = CarOwner.objects.all()
# licence = DriverLicence.objects.order_by("recieved_date").values("owner_id", "recieved_date")
# result = [f"{i} {licence.filter(owner_id=i).values('recieved_date')}" for i in owners]
# print(result)