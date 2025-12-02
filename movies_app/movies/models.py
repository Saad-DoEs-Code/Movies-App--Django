from django.db import models

# Create your models here.
class Movie(models.Model):
    
    name = models.CharField(max_length=60)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="Images/", default="Images/None/NoImg.jpg")
    
    def __str__(self):
        return self.name 