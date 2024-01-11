## Models 

В ходе выполнения работы были реализованы все модели, необходимые для успешного создания полного функционала лабораторной работы. Более подробно рассмотреть модели можно в коде в папке лабораторной.

### Пример:

- Модель животного - самая большая модель в коде. Она имеет в себе не только текст и числа, но и выбор (пол m или f), а также дату (день рождения) и несколько fk из моделей с диетами и местами для зимовки.

```python
class Animal(models.Model):
    num = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=500)
    age = models.IntegerField()
    sex = models.TextField(max_length=2, choices=(('m', 'm'), ('f', 'f')))
    birthdate = models.DateField()
    diet = models.ForeignKey('system.Diet', related_name='animals_on_this_diet', on_delete=models.CASCADE,
                             null=True, blank=True)

    winter_place = models.ForeignKey('system.WinterPlace', related_name='birds_wintering', on_delete=models.CASCADE,
                                     null=True, blank=True)

    winter_sleeping = models.IntegerField(null=True, blank=True)
    normal_temperature = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
```