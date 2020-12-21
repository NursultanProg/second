from django.conf import settings
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    tittle = models.CharField(max_length = 255)
    text = models.TextField()
    def publish(self):
        self.save()
    
    def __str__(self):
        return self.title