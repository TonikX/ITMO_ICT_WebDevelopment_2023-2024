from django.db import models
from .user import User
from .article import Article


class Role(models.Model):
    """ Роль пользователя в создании контента """
    name = models.CharField(max_length=250, null=False, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Participant(models.Model):
    """ Какую конкретно роль пользователь сыграл при создании """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья")
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Фактическая роль")

    def save(self, *args, **kwargs):
        # Check if the user is a team member before saving
        if self.user.is_team_member:
            super().save(*args, **kwargs)
        else:
            raise ValueError("Можно добавить только тех пользователей, которые являются членами команды")

    class Meta:
        verbose_name = "Участие в создании"
        verbose_name_plural = "Участие в создании"

# выбор делать только по активным пользователям и по полномочиям
