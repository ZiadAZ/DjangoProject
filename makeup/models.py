from django.db import models

# Create your models here.class Question(models.Model):
class Brand(models.Model):
    name = models.CharField(max_length=10)
    orgin = models.CharField(max_length=200)

    def getUrl(self):
        return '/makeup/brand/{0}'.format(self.id)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    descreption = models.CharField(max_length=250)
    expirDate= models.DateField()
    price=models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def getUrl(self):
        return '/makeup/product/{0}'.format(self.id)