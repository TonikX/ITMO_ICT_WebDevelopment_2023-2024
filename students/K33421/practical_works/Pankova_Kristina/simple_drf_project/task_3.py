from django.db.models import Min, Max
DriversLicence.objects.aggregate(oldest_licence=Min('date_begin'))


from django.db.models import Count
counter_cars=CarOwner.objects.annotate(Count("car"))
for owner in counter_cars:
    print(owner.username, owner.car__count)

Car.objects.values("model").annotate(Count("id"))
