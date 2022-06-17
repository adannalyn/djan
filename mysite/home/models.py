from django.db import models

# Create your models here.
class OurCustomer(models.Model):
    username = models.CharField(max_length = 50)
    user_fname = models.CharField(max_length = 10000)
    user_lname = models.CharField(max_length = 10000)
    user_email = models.EmailField(max_length = 10000)
    
    def __str__(self):
        return self.username
class Post(models.Model):
    post_title = models.CharField(max_length = 10000)
    post_content = models.CharField(max_length = 10000)
    author = models.ForeignKey(OurCustomer, on_delete=models.CASCADE, default=1)
    date_posted = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.post_title
    
class Profile(models.Model):
    bio = models.CharField(max_length=10000)
    user = models.OneToOneField(OurCustomer, on_delete=models.CASCADE)
    
    

