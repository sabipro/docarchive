from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def documentation(request):
    return HttpResponse("documentation")
