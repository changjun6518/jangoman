from django.db import models

# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)


class Author(models.Model):
    name = models.CharField(max_length = 200)
    nationarity = models.CharField(max_length = 200)


class Book(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete = models.CASCADE,
        related_name = 'books',
    )
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
        related_name = 'books'
    )

    title = models.CharField(max_length = 200)


# 책이 어느 도서관에 몇개 있는지에 대한 걸 만들 순 없는가?


class Page(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete = models.CASCADE,
        related_name = 'pages',
    )

    text = models.TextField(null=True, blank = True)
    page_number = models.IntegerField()



class Language(models.Model):
    book = models.OneToOneField(
        Book,
        on_delete = models.CASCADE,
    )

    language = models.CharField(max_length = 200)