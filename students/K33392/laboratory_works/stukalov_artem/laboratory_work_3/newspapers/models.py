from django.db import models


class Newspaper(models.Model):
    name = models.CharField(max_length=100)
    publication_index = models.CharField(max_length=100)
    redactor_full_name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.publication_index}"


class PrintingOffice(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.address}"


class PostOffice(models.Model):
    index = models.IntegerField(unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.index} {self.address}"


class NewspaperEdition(models.Model):
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    printing_office = models.ForeignKey(PrintingOffice, on_delete=models.CASCADE)

    amount = models.IntegerField()

    def __str__(self):
        return f"{self.newspaper.name} {self.printing_office.name}"


class NewspaperOrder(models.Model):
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE)

    amount = models.IntegerField()

    def __str__(self):
        return f"{self.newspaper.name} {self.post_office.index}"


class NewspaperDistribution(models.Model):
    edition = models.ForeignKey(NewspaperEdition, on_delete=models.CASCADE)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE)

    amount = models.IntegerField()

    def __str__(self):
        return f"{self.edition.newspaper.name} {self.post_office.index}"
