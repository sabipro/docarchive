from django.contrib import admin
from bibliotheque.models import Users,Ouvrages,Categorie,Directeurs

# Register your models here.
admin.site.register(Users)
admin.site.register(Ouvrages)

admin.site.register(Categorie)
admin.site.register(Directeurs)
