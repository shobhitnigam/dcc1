from django.db import models

# Create your models here.

class contest(models.Model):
    
    gametype = models.CharField(max_length=100)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    mdate = models.DateTimeField()
    cfee = models.DecimalField(max_digits=20, decimal_places=10
    )