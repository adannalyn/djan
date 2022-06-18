from django.db import models
from datetime import date

class GuestProfile(models.Model):
    occupant_name=models.CharField(max_length=100)
    occupant_occupation=models.CharField(max_length=100)
    occupant_email=models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
class Rooms(models.Model):
    room_no=models.CharField(max_length=5)
    price=models.FloatField(default=1000.00)
    no_of_nights=models.IntegerField()
    def __str__(self):
        return "Room No: " +str(self.id)

class Booking(models.Model):
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    def is_past_due(self):
        return date.today()>self.end_day

