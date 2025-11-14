from django.http.response import HttpResponse
from django.shortcuts import render


def accueil(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")
