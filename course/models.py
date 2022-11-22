from django.db import models

class DestCommonInfo(models.Model):
    place = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    # ID PLACE COUNTRY TIME PRICE
    country = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    time = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    price = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    slug = models.SlugField(max_length=255, unique=True, blank=False, null=True)

# Create your models here.
class Destination(models.Model):

    def __str__(self):
        return self.place

    class Meta:
        db_table = 'destination'

#class CourseClass(models.Model):
