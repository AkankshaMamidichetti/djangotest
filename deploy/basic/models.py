from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    course=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    registered_at=models.DateField(auto_now_add=True)