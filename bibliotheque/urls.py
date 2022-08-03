from django.urls import path
from . import views

urlpatterns = [
    path('bibliotheque/', views.bibliotheque,name="bibliotheque"),
    


]