from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel  # https://django-polymorphic.readthedocs.io/en/latest/


def get_curr_time_plus_interval(interval_minutes=5):
    """ Функция для установки значения по умолчанию для datetime_published """
    return timezone.now() + timezone.timedelta(minutes=interval_minutes)


# display only if (is_piblished and not is_hidden)
class ContentObject(PolymorphicModel):
    """ Базовый объект контента """
    name = models.CharField(max_length=250, null=False, verbose_name="Название")
    short_description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Краткое описание")
    cover_picture = models.ImageField(
        upload_to='images/content_object/',
        null=True,
        default='images/alt_image.jpg',
        verbose_name="Изображение"
    )
    datetime_published = models.DateTimeField(null=False, default=get_curr_time_plus_interval,
                                              verbose_name="Дата и время публикации")
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата создания")
    is_hidden = models.BooleanField(null=False, default=False, verbose_name="Скрыть объект")

    # TODO: add the n_views field and write the logic for auto-update

    @property
    def is_published(self) -> bool:
        """ Проверка, опубликован ли объект """
        return self.datetime_published <= timezone.now()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Базовый объект контента"
        verbose_name_plural = "Базовые объекты контента"
