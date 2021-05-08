from django.db import models

# Create your models here.
class Property(models.Model):

    RENT = 'Rent'
    SALE = 'Sale'
    TYPES_OF_PROPERTY_CHOICES = [(RENT, 'Rent'),(SALE, 'Sale')]
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 80, null = True)
    property_type = models.CharField(choices = TYPES_OF_PROPERTY_CHOICES, max_length = 10, default = SALE)
    price = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places = 0, max_digits = 5)
    category = models.ForeignKey('Category', null = True, on_delete = models.SET_NULL)
    number_of_rooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()
    number_of_parking = models.PositiveIntegerField()
    image = models.ImageField(upload_to='Property/images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):

    name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to='Property/images/', null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Reserve(models.Model):

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name