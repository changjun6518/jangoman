from django.db import models

# Create your models here.


class Library(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)


    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length = 200)
    nationarity = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Language(models.Model):

    language = models.CharField(
        max_length = 200,
        default = '',
        )

    def __str__(self):
        return self.language


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
    language = models.ForeignKey(
        Language,
        on_delete = models.CASCADE,
        default = '',
        related_name = 'books'
    )

    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title


# 책이 어느 도서관에 몇개 있는지에 대한 걸 만들 순 없는가?


class Page(models.Model):
    book = models.OneToOneField(
        Book,
        on_delete = models.CASCADE,
        related_name = 'pages',
    )

    text = models.TextField(null=True, blank = True)
    page_number = models.IntegerField()

    def __str__(self):
        return self.page_number

 
