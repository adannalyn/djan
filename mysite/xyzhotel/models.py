from django.db import models
from datetime import dateclass 

class Contact(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    def __str__(self):
        return self.nameclass

class Rooms(models.Model):
    manager=models.ForeignKey(User, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5, )
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=1000.00)
    no_of_nights=models.IntegerField()
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, 
    max_length=None,default='0.jpeg')
    def __str__(self):
        return "Room No: "+str(self.id)
class Booking(models.Model):
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id=models.ForeignKey(Contact, on_delete=models.CASCADE)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    amount=models.FloatField()
    booked_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return “Booking id: " +str(self.id)
    def is_past_due(self):
        return date.today()>self.end_day 
