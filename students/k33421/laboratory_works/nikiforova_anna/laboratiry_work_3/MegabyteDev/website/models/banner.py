from django.db import models
from .article import Article
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class Banner(models.Model):
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Статья")
    n_amongst_banners = models.IntegerField(null=False, default=1, unique=True,
                                            validators=[MinValueValidator(1), MaxValueValidator(settings.N_BANNERS)],
                                            verbose_name="Номер баннера")
    special_cover_picture = models.ImageField(upload_to='images/banner/', null=True, blank=True,
                                              verbose_name="Специальная картинка обложки")

    @property
    def cover_picture(self):
        return self.special_cover_picture if self.special_cover_picture else self.article.cover_picture

    def __str__(self):
        return "Баннер " + str(self.n_amongst_banners)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

        constraints = [
            models.CheckConstraint(
                check=models.Q(n_amongst_banners__gte=1) & models.Q(n_amongst_banners__lt=settings.N_BANNERS),
                name=f"Может быть только {settings.N_BANNERS} последовательных баннеров",
            )
        ]
