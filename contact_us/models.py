from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    problem = models.TextField( )
    
    
    def clean(self):
        if not self.phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")
    
    def __str__(self):
        return self.name
    