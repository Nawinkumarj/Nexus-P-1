from django.db import models

# Create your models here.
class values(models.Model):
    Fname = models.CharField(max_length=20, default="")
    Lname = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return f"{self.Fname} {self.Lname}" 
    