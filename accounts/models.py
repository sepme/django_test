from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    book_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    book_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
