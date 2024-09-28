from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name



class Phone(models.Model):
    model = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    price = models.IntegerField()
    photos = models.ImageField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.model