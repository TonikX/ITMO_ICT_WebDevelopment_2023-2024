from django.db import models


class Rubric(models.Model):
    """ Рубрика """
    name = models.CharField(max_length=250, null=False, unique=True, verbose_name="Название")
    short_description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Краткое описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Рубрика"
        verbose_name_plural = "Рубрики"


class Hashtag(models.Model):
    """ Хэштэг """
    name = models.CharField(max_length=250, null=False, unique=True, verbose_name="Название")
    hashtag_articles = models.ManyToManyField('Article', through='Hashtags', verbose_name="Статьи")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Хэштег"
        verbose_name_plural = "Хэштеги"
