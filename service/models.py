from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images")
    


BLOOD_TYPES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]
class bloodmodel(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="service/images/")
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    bloodgroup = models.CharField(choices = BLOOD_TYPES, max_length=10 )
     
 
 
class TestModel(models.Model):
    name = models.CharField(max_length=20 )
    image = models.ImageField(upload_to="service/images/")
    cost = models.IntegerField()
    
    def __str__(self):
        return self.name


class testBook(models.Model):
    test = models.ForeignKey(TestModel, on_delete= models.CASCADE, verbose_name="Test")
    name = models.CharField(max_length=100, verbose_name="Customer Name")
    phone = models.CharField(max_length=50,  verbose_name="Customer Phone")
    email = models.CharField(max_length=50 ,  verbose_name="Customer Email")
    
    def __str__(self):
        return f"{self.name} - {self.test.name}"
 