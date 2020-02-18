from django.db import models

# Create your models here.
""" model for books """
class Book(models.Model):
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    genre = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    """ used to define if books checked in or out """
    checkedOut = models.BooleanField(default=False)
    """ used to police check-in  / out function and ensure that books can only be returned by original borrower """
    checked_by = models.CharField(max_length=254, default='', blank=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        