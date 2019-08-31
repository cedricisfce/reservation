from django.db import models

# Create your models here.
class Artist(models.Model):
    id = models.BigAutoField
    firstname = models.CharField(max_length=60, help_text="Prénom de l'artiste")
    lastname = models.CharField(max_length=60, help_text="Nom de l'artiste")

    def __str__(self):
        return self.id

class Types(models.Model):
    id = models.BigAutoField
    type = models.CharField(max_length=60)

    def __str__(self):
        return self.id

class ArtistType(models.Model):
    id = models.BigAutoField
    artist_id = models.ForeignKey('Artist',on_delete=models.CASCADE)
    type_id = models.ForeignKey('Types', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Localities(models.Model):
    id = models.BigAutoField
    post_code = models.CharField(max_length=6, help_text="Code Postal", unique=True)
    locality = models.CharField(max_length=60, help_text="Désignation officiel de la localité", unique=True)

class Locations(models.Model):
    id = models.BigAutoField
    locality_id = models.ForeignKey('Localities',on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=60, help_text="Label court d'identification", unique=True)
    designation = models.CharField(max_length=60, help_text="Titre du spectale", null=True)
    address = models.CharField(max_length=255, help_text="URL de l'affiche", null=True)
    website = models.BooleanField(help_text="Réservable ou non")
    phone = models.FloatField(help_text="Prix du Spectacle")

class Shows(models.Model):
    id = models.BigAutoField
    location_id = models.ForeignKey('Locations', help_text="id du lieu de (locations)",null=True)
    slug = models.SlugField(max_length=60, help_text="Label court d'identification", unique=True)
    title = models.CharField(max_length=255, help_text="Titre du spectale", null=True)
    poster_url = models.CharField(max_length=255, help_text="URL de l'affiche", null=True)
    bookable = models.BooleanField(help_text="Réservable ou non")
    price = models.FloatField(help_text="Prix du Spectacle")
    description = models.CharField(help_text="Description du spectacle")
    created_at = models.DateField(auto_now_add=True, help_text="Date de création")


class Shows(models.Model):
    id = models.BigAutoField
    location_id = models.ForeignKey()




