from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    authur = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post_title
    def snippet(self):
        return self.post_content [:200] + '...'
    
    