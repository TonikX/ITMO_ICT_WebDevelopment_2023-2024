from django.db import models
from .user import User
from .content_object import ContentObject


class Favourite(models.Model):
    """ Избранное """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    content_object = models.ForeignKey(ContentObject, on_delete=models.CASCADE, verbose_name="Объект контента")

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
