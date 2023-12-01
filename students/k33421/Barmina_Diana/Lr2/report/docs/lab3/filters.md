# Создание специальных фильтров

**Фильтр для списка восхождений**</br>
<br/> Добавлена дополнительная сортировка по минимальной и максимальной цене и по промежутку в днях. Также имеется базовый фильтр по горе, клубу-организатору и уровню сложности восхождения

```

class ClimbingsFilter(filters.FilterSet):
    min_cost = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    max_cost = filters.NumberFilter(field_name="cost", lookup_expr='lte')
    min_date = filters.DateFilter(field_name="start_date_plan", lookup_expr='gte')
    max_date = filters.DateFilter(field_name="finish_date_plan", lookup_expr='lte')

    class Meta:
        model = Climbing
        fields = ['club_id', 'mountain_id', 'level']

```
**Фильтр для списка гор**</br>
<br/> Добавлена дополнительная сортировка по минимальной и максимальной высоте. Также имеется базовый фильтр по имени и стране нахождения

```

class MountainsFilter(filters.FilterSet):
    min_height = filters.NumberFilter(field_name='hight', lookup_expr='gte')
    max_height = filters.NumberFilter(field_name='hight', lookup_expr='lte')

    class Meta:
        model = Mountain
        fields = ['name', 'state']

```
