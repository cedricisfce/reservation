from django.db import models

# Create your models here.
class Artist(models.Model):
    id = models.BigAutoField
    firstname = models.CharField(max_length=60, help_text="Prénom de l'artiste")
    lastname = models.CharField(max_length=60, help_text="Nom de l'artiste")

    def __str__(self):
        return "{} - {}".format(self.firstname, self.lastname)

class Types(models.Model):
    id = models.BigAutoField
    type = models.CharField(max_length=60)

    def __str__(self):
        return self.type

class ArtistType(models.Model):
    id = models.BigAutoField
    artist_id = models.ForeignKey('Artist',on_delete=models.CASCADE)
    type_id = models.ForeignKey('Types', on_delete=models.CASCADE)

    def __str__(self):
        return self.artist_id.name

class Localities(models.Model):
    id = models.BigAutoField
    post_code = models.CharField(max_length=6, help_text="Code Postal", unique=True)
    locality = models.CharField(max_length=60, help_text="Désignation officiel de la localité", unique=True)

    def __str__(self):
        return self.locality

class Locations(models.Model):
    id = models.BigAutoField
    locality_id = models.ForeignKey('Localities',on_delete=models.CASCADE,null=True)
    slug = models.SlugField(max_length=60, help_text="Label court d'identification", unique=True)
    designation = models.CharField(max_length=60, help_text="Désignation officiel du lieu", null=True)
    address = models.CharField(max_length=255, help_text="Addresse du lieu", null=True)
    website = models.CharField(max_length=255, help_text="Site web du lieu", null=True)
    phone = models.CharField(max_length=60, help_text="Numéro de téléphone du lieu", null=True)

    def __str__(self):
        return self.designation

class Shows(models.Model):
    id = models.BigAutoField
    location_id = models.ForeignKey('Locations', on_delete=models.CASCADE, help_text="id du lieu de (locations)",null=True)
    slug = models.SlugField(max_length=60, help_text="Label court d'identification", unique=True)
    title = models.CharField(max_length=255, help_text="Titre du spectale", null=True)
    poster_url = models.CharField(max_length=255, help_text="URL de l'affiche", null=True)
    bookable = models.BooleanField(help_text="Réservable ou non")
    price = models.FloatField(help_text="Prix du Spectacle")
    description = models.CharField(max_length=255,help_text="Description du spectacle")
    created_at = models.DateField(auto_now_add=True, help_text="Date de création")

    def __str__(self):
        return self.title

class Collaborations(models.Model):
    id = models.BigAutoField
    artist_type_id = models.ForeignKey('ArtistType',on_delete=models.CASCADE, help_text="id de l'artiste associé à un type (fonction)")
    show_id = models.ForeignKey('Shows',on_delete=models.CASCADE , help_text="id du spectacle")

    def __str__(self):
        return self.artist_type_id.name

class Roles(models.Model):
    id = models.BigAutoField
    role = models.CharField(max_length=30, help_text="role")

    def __str__(self):
        return self.role

class Users(models.Model):
    id = models.BigAutoField
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    role_id = models.ForeignKey('Roles', on_delete=models.CASCADE, help_text="id du role")
    firstname = models.CharField(max_length=60, help_text="Prénom de l'artiste")
    lastname = models.CharField(max_length=60, help_text="Nom de l'artiste")
    email = models.EmailField(help_text="E-mail")
    langue = models.CharField(max_length=2, help_text="langue de l'utilisateur")

    def __str__(self):
        return self.login

class Representations(models.Model):
    id = models.BigAutoField
    show_id = models.ForeignKey('Shows', on_delete=models.CASCADE, help_text="id du show")
    when = models.DateTimeField(help_text="Date de la représentation")
    location_id = models.ForeignKey('Locations',on_delete=models.CASCADE, help_text="id du lieu de (locations)", null=True)

    def __str__(self):
        return self.when

class RepresentationUser(models.Model):
    id = models.BigAutoField
    representation_id = models.ForeignKey('Representations', on_delete=models.CASCADE, help_text="id de la représentation")
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE, help_text="id de l'utilisateur")
    places = models.IntegerField(help_text="Nombre de places")

    def __str__(self):
        return str(self.id)








