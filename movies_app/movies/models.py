from django.db import models

# Create your models here.
class Movie(models.Model):
    
    name = models.CharField(max_length=60)
    duration = models.FloatField()
    rating = models.FloatField()
    
    def __str__(self):
        return self.name 