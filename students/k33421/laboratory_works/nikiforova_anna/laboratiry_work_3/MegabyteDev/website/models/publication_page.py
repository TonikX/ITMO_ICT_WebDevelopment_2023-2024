from django.core.validators import MinValueValidator
from django.db import models
from .publication import Publication
from .article import Article


class PublicationPage(models.Model):
    """ Отдельная страница публикации """
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name='Публикация "на бумаге"')
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE,
                                verbose_name="Связанная со страницей статья")
    n_amongst_pages = models.IntegerField(null=False, validators=[MinValueValidator(1)],
                                          verbose_name="Номер страницы в выпуске")
    attached_page_file = models.FileField(null=False, upload_to="files/publication_pages/",
                                          verbose_name="Файл (pdf/png/jpg)")

    def __str__(self):
        return str(self.article) + ' стр. ' + str(self.n_amongst_pages)

    class Meta:
        verbose_name = "Отдельная страница публикации"
        verbose_name_plural = "Отдельные страницы публикации"

        unique_together = ('publication', 'n_amongst_pages')
        constraints = [
            models.CheckConstraint(
                check=models.Q(n_amongst_pages__gte=1),
                name=f"Номер страницы должен быть положительным числом",
            )
        ]
