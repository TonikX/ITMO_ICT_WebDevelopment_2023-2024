from django.core.validators import MinValueValidator
from django.db import models

from .content_object import ContentObject


class Podcast(models.Model):
    """ Подкаст (как совокупность выпусков) """
    name = models.CharField(max_length=250, null=False, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    cover_picture = models.ImageField(upload_to='images/podcast/', null=True,
                                      default='images/alt_image.jpg',
                                      verbose_name="Изображение")
    podcast_platforms = models.ManyToManyField('Platform', through='PodcastLink', verbose_name="Платформы")

    @property
    def issues_count(self):
        return self.podcast_issues.count()

    @property
    def last_published_issue(self):
        return self.podcast_issues.latest('release_date').release_date

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкаст"
        verbose_name_plural = "Подкасты"


class Platform(models.Model):
    """ Внешняя платформа, на которой есть подкаст """
    name = models.CharField(max_length=250, null=False, verbose_name="Название")
    base_reference_link = models.URLField(null=True, blank=True, verbose_name="Ссылка на платформу")

    class Meta:
        verbose_name = "Платформа"
        verbose_name_plural = "Платформы"

    def __str__(self):
        return self.name


class PodcastLink(models.Model):
    """ Ссылка на внешний источник, где можно слушать подкаст """
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, verbose_name="Подкаст")
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT, verbose_name="Платформа")
    external_reference_link = models.URLField(null=False, verbose_name="Ссылка на подкаст на платформе")

    class Meta:
        verbose_name = "Внешняя ссылка на подкаст"
        verbose_name_plural = "Внешние ссылки на подкаст"

    def __str__(self):
        return str(self.platform) + ', ' + str(self.podcast)


class PodcastIssue(ContentObject):
    """ Выпуск подкаста """
    podcast = models.ForeignKey(Podcast, related_name='podcast_issues', on_delete=models.PROTECT,
                                verbose_name="Подкаст")
    n_issue = models.IntegerField(null=False, verbose_name="Номер выпуска", validators=[MinValueValidator(1)])
    audio_file = models.FileField(upload_to='files/podcasts/', verbose_name="Аудиофайл")  # пока как заглушка

    class Meta:
        verbose_name = "Выпуск подкаста"
        verbose_name_plural = "Выпуски подкаста"

        unique_together = ('podcast', 'n_issue')
        constraints = [
            models.CheckConstraint(
                check=models.Q(n_issue__gte=1),
                name=f"Номер подкаста должен быть положительным числом",
            )
        ]
