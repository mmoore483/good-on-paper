from django.db import models


class Book(models.Model):
    book_id = models.CharField(max_length=254, null=False, blank=False)
    title = models.CharField(max_length=254, null=False, blank=False)
    series = models.CharField(max_length=254, null=True, blank=True)
    author = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    genres = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    first_published_year = models.CharField(
        max_length=254, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    isbn = models.CharField(max_length=254, null=True, blank=True)
    isbn13 = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=False)

    def __str__(self):
        return self.title
