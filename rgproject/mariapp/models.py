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

class Department(models.Model):  # 1HR 2Sales 3Purchase
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

# one to many relationship
class Employee(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.department.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title + " " + self.description

