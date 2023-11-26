from django.db import models
from .content_object import ContentObject


class Publication(ContentObject):  # it is Polymorphic too
    """ Базовая публикация на бумаге """
    attached_file = models.FileField(null=True, blank=True, upload_to="files/publications/", verbose_name="Файл (pdf)")
    external_reference_link = models.URLField(null=True, blank=True, verbose_name="Ссылка на внешний источник")

    class Meta:
        verbose_name = 'Публикация "на бумаге"'
        verbose_name_plural = 'Публикации "на бумаге"'


class Newtone(Publication):
    """ Журнал """

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"


class Newspaper(Publication):
    """ Газета """

    class Meta:
        verbose_name = "Газета"
        verbose_name_plural = "Газеты"
