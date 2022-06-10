from django.db import models

class People(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    occupation = models.CharField(max_length=200)

    def __str__(self):
        return "%s the people" % self.name

class Doctor(models.Model):
    patients = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    can_see_patients = models.BooleanField(default=False)
    can_see_patients = models.BooleanField(default=False)

    def __str__(self):
        return "%s the doctor at" % self.place.name

class Address(models.Model):
    local = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    foreign = models.CharField(max_length=50)

    def __str__(self):
        return "%s the address at %s" % (self.name, self.restaurant)
class Product(models.Model):
    sales = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    promo = models.CharField(max_length=50)

    def __str__(self):
        return "%s the product available %s" % (self.name, self.restaurant)