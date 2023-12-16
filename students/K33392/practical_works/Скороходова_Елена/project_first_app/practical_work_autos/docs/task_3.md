#Задание 3

Необходимо реализовать следующие запросы c применением описанных методов:
Вывод даты выдачи самого старшего водительского удостоверения
Укажите самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
Выведите количество машин для каждого водителя
Подсчитайте количество машин каждой марки
Отсортируйте всех автовладельцев по дате выдачи удостоверения (Примечание: чтобы не выводить несколько раз одни и те же таблицы воспользуйтесь методом .distinct()


###Ход выполнения:

Настраиваем среду выполнения Django, а также импортируем необходимые методы (Min, Max, Count) 
для агрегации и аннотации запросов.

Выполним запросы к базе данных для получения:

Самой ранней даты выдачи водительских удостоверений.
Самой поздней даты начала владения автомобилем.
Количества машин для каждого владельца.
Количества машин для каждой марки автомобиля.
Владельцев, отсортированных по дате начала владения автомобилем.

    import os
    
    import django
    from django.db.models import Min, Max, Count
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_first_app.settings")
    django.setup()
    
    from blog.models import CustomUser, Auto, Ownership, DrivingLicence
    
    oldest_licence = DrivingLicence.objects.aggregate(max_start_date=Min("start_date"))["max_start_date"]
    
    newest_ownership = Ownership.objects.aggregate(max_start_date=Max("start_date"))["max_start_date"]
    
    ownerships_counts = CustomUser.objects.annotate(count=Count("ownerships"))
    ownerships_counts_str = [f"{owner.full_name}: {owner.count}" for owner in ownerships_counts]
    
    cars_count_by_brands = Auto.objects.values("brand").annotate(count=Count("id"))
    cars_count_by_brands_str = [f"{car['brand']}: {car['count']}" for car in cars_count_by_brands]
    
    sorted_owners = CustomUser.objects.order_by("ownerships__start_date").all()
    
    print(
        f"Дата самого старшего удостоверения: {oldest_licence}",
        f"Самая поздняя дата авто владения: {newest_ownership}",
        f"Количество машин для каждого водителя: {ownerships_counts_str}",
        f"Количество машин каждой марки: {cars_count_by_brands_str}",
        f"Автовладельцы, отсортированные по дате выдачи удостоверения: {sorted_owners}",
        sep="\n\n",
    )

Вывод в консоль:

![Задание 3](img\task_3.PNG)