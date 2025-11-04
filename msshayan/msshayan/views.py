from django.http.response import HttpResponse


def accueil(request):
    return HttpResponse("Bienvenue, ceci est le contenu de la page Accueil")


def contact(request):
    return HttpResponse("Bienvenue, ceci est le contenu de la page Contact")
