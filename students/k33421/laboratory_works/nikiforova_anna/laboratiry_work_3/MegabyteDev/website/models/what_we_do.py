from django.db import models


class WhatWeDo(models.Model):
    """ Что мы делаем помимо представленного на сайте """
    name = models.CharField(max_length=250, null=False, verbose_name="Название")
    short_description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Краткое описание")
    cover_picture = models.ImageField(
        upload_to='images/what_we_do/',
        null=True,
        default='images/alt_image.jpg',
        verbose_name="Изображение"
    )
    external_reference_link = models.URLField(null=True, blank=True, verbose_name="Внешняя ссылка")
    # is_displayed = models.BooleanField(null=False, default=False, verbose_name="Отображается на сайте сейчас")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Что мы делаем"
        verbose_name_plural = "Что мы делаем"
