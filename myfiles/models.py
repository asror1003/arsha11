from django.db import models

# Create your models here.
class Type(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Portfolio(models.Model):
    nomi = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    date = models.DateField()
    url = models.URLField()
    malumot = models.TextField()
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)

class Murojat(models.Model):
    nomi = models.CharField(max_length=30)
    mail = models.EmailField(max_length=40)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField()

class Team(models.Model):
    ismi = models.CharField(max_length=30)
    lavozimi = models.CharField(max_length=40)
    malumot = models.TextField()
    twitter = models.CharField(max_length=40)
    facebook = models.CharField(max_length=40)
    instagram = models.CharField(max_length=40)
    inn = models.CharField(max_length=40)
    rasm = models.ImageField(upload_to='media')