from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    height = models.FloatField(default=0.0)

class Product(models.Model):
    name = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='userImage/')

    def __str__(self):
        return "Product: "+str(self.name)+" "+str(self.price)+" "+str(self.description)+" "+str(self.image)

