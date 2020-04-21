from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

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
    
    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.OneToOneField(
        Book,
        on_delete = models.CASCADE,
    )

    page_length = models.IntegerField()

    def __str__(self):
        return self.page_length