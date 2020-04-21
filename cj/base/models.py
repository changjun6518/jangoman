from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length = 200)


class Author(models.Model):
    name = models.CharField(max_length = 200)


class Language(models.Model):
    name = models.CharField(max_length = 200)

class Book(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete = models.CASCADE,
    )
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
    )
    language = models.ForeignKey(
        Language,
        on_delete = models.CASCADE,
    )

    title = models.CharField(max_length=200)
    


class Page(model.Model):
    book = models.OneToOneField(
        Book,
        on_delete = models.CASCADE,
    )

    page_length = models.IntegerField()