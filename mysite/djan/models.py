from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Doctor(models.Model):
    patients = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    can_see_patients = models.BooleanField(default=False)
    can_see_patients = models.BooleanField(default=False)

    def __str__(self):
        return "%s the doctor at" % self.place.name

class Address(models.Model):
    local = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    foreign = models.CharField(max_length=50)

    def __str__(self):
        return "%s the address at %s" % (self.name, self.doctor)
class Product(models.Model):
    productname = models.CharField(max_length=200,default="")
    price = models.DecimalField(max_digits=5,decimal_places=2, default=0)