from django.db import models

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=10000)
    post_content = models.CharField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)

