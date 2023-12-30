from .models import Car, CarOwning, Owner, License
import datetime

car1 = Car.objects.create(num='num1', mark='mark1', model='model1', color='black')
car2 = Car.objects.create(num='num2', mark='mark1', model='model2', color='black')
car3 = Car.objects.create(num='num3', mark='mark1', model='model3', color='black')
car4 = Car.objects.create(num='num4', mark='mark2', model='model1', color='black')
car5 = Car.objects.create(num='num5', mark='mark2', model='model2', color='black')
car6 = Car.objects.create(num='num6', mark='mark2', model='model3', color='black')

license1 = License.objects.create(name='licence1', owner=car1, license_type='type1', date_given=datetime.date.today())
license2 = License.objects.create(name='licence2', owner=car2, license_type='type1', date_given=datetime.date.today())
license3 = License.objects.create(name='licence3', owner=car3, license_type='type1', date_given=datetime.date.today())
license4 = License.objects.create(name='licence4', owner=car4, license_type='type2', date_given=datetime.date.today())
license5 = License.objects.create(name='licence5', owner=car5, license_type='type2', date_given=datetime.date.today())

owner1 = Owner.objects.create(name='name1', surname='surname1', birthday=datetime.date.today())
owner2 = Owner.objects.create(name='name2', surname='surname2', birthday=datetime.date.today())
owner3 = Owner.objects.create(name='name3', surname='surname3', birthday=datetime.date.today())
owner4 = Owner.objects.create(name='name4', surname='surname4', birthday=datetime.date.today())
owner5 = Owner.objects.create(name='name5', surname='surname5', birthday=datetime.date.today())
owner6 = Owner.objects.create(name='name6', surname='surname6', birthday=datetime.date.today())

car_owing1 = CarOwning.objects.create(start=datetime.date.today(), finish=datetime.date.today(),
                                      car=car1, owner=owner1)
car_owing2 = CarOwning.objects.create(start=datetime.date.today(), finish=datetime.date.today(),
                                      car=car2, owner=owner2)
car_owing3 = CarOwning.objects.create(start=datetime.date.today(), finish=datetime.date.today(),
                                      car=car3, owner=owner3)
car_owing4 = CarOwning.objects.create(start=datetime.date.today(), finish=datetime.date.today(),
                                      car=car4, owner=owner4)
car_owing5 = CarOwning.objects.create(start=datetime.date.today(), finish=datetime.date.today(),
                                      car=car5, owner=owner5)
car_owing6 = CarOwning.objects.create(start=datetime.date.today(), finish=datetime.date.today(),
                                      car=car6, owner=owner6)


####

#Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)

qs = Car.objects.filter(mark='mark1')
print(qs)

#Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)

qs = Owner.objects.filter(name='name1')
print(qs)

#Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)

owner = Owner.objects.all().first()
licence = License.objects.filter(owner=owner)
print(licence)

#Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)
qs = Car.objects.filter(color='black')
print(qs)

#Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)

qs = Owner.objects.filter(cars__start__gt=datetime.date(year=2010, month=1, day=1),
                          cars__start__lt=datetime.date(year=2011, month=1, day=1))
print(qs)


#####
from django.db.models import Min, Max, Count


#Вывод даты выдачи самого старшего водительского удостоверения

res = License.objects.aggregate(date_given=Min('date_given'))
print(res)

#Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе

res = CarOwning.objects.aggregate(date_given=Max('finish'))
print(res)

#Выведите количество машин для каждого водителя

counts = Owner.objects.annotate(Count("cars"))
for count in counts:
    print(owner.name, count.cars__count)

#Подсчитайте количество машин каждой марки

counts = Car.objects.annotate(Count("mark"))
for count in counts:
    print(count.num, count.mark__count)

#Отсортируйте всех автовладельцев по дате выдачи удостоверения

qs = License.objects.order_by("date_given")
print(qs)
