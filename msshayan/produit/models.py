from django.db import models

# Create your models here.


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    image = models.FileField(upload_to="static/images/produits")
    description = models.CharField(max_length=255)
