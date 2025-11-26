from django.http.response import HttpResponse
from django.shortcuts import render
from produit.models import Produit


def accueil(request):
    all_product = Produit.objects.all()
    return render(request, "index.html", {"products": all_product})


def contact(request):
    return render(request, "contact.html")
