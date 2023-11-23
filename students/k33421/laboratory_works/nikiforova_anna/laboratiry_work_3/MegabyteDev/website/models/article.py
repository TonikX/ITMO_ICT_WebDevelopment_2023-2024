from django.db import models
from functools import cached_property
from .content_object import ContentObject
from .rubric import Rubric, Hashtag
from ckeditor_uploader.fields import RichTextUploadingField


class Article(ContentObject):
    """ Статья """
    content = RichTextUploadingField(verbose_name="Содержание")
    rubric = models.ForeignKey(Rubric, related_name='articles', null=False,
                               on_delete=models.PROTECT, verbose_name="Рубрика")
    article_hashtags = models.ManyToManyField('Hashtag', through='Hashtags', verbose_name="Хэштеги")
    article_participants = models.ManyToManyField('User', through='Participant', verbose_name="Участники в создании")

    # @cached_property
    # def time_required_for_reading(self):
    # TODO: write the logic for counting reading time
    # TODO: add keywords for simple recommendations

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Hashtags(models.Model):
    """ Хэштеги статьи """
    article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Статья")
    hashtag = models.ForeignKey('Hashtag', on_delete=models.CASCADE, verbose_name="Хэштег")

    class Meta:
        verbose_name = "Хэштег у статьи"
        verbose_name_plural = "Хэштеги у статей"

