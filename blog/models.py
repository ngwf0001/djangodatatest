from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.title} -- by  {self.author.firstname} {self.author.lastname}'
    
