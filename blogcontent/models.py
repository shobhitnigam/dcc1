from django.db import models

# Create your models here.
class newblog(models.Model):
    blognew = models.TextField()
    name=models.CharField(max_length=100)