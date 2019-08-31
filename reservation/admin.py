from django.contrib import admin

from reservation.models import *
# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtistType)
class ArtistTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Collaborations)
class CollaborationsAdmin(admin.ModelAdmin):
    pass

@admin.register(Localities)
class LocalitiesAdmin(admin.ModelAdmin):
    pass

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    pass

@admin.register(Representations)
class RepresentationsAdmin(admin.ModelAdmin):
    pass

@admin.register(RepresentationUser)
class RepresentationUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    pass

@admin.register(Shows)
class ShowsAdmin(admin.ModelAdmin):
    pass

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    pass

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass


