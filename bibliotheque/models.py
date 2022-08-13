from django.db import models

# Create your models here.

from sre_constants import CATEGORY
from unicodedata import category
from django.db import models


# Create your models here.
class Users(models.Model):
    nom= models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pasword = models.CharField(max_length=50)
    telephone = models.IntegerField()


    def __str__(self):
        return self.nom



class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=50)


    def __str__(self):
        return self.nom_categorie




class Ouvrages(models.Model):
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    desciption = models.TextField()
    couverture = models.ImageField(upload_to="images/",blank=True)
    date_parition = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    
    category= models.ForeignKey(Categorie,  on_delete=models.CASCADE)
    users = models.ManyToManyField(Users)


    def __str__(self):
        return self.auteur




class Directeurs(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    period_nomination = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images",blank=True)
    biographie = models.TextField(),


    def __str__(self):
        return self.nom




    
