from django.shortcuts import render
from .models import Artigo


def lista_artigos(request):
    artigos = Artigo.objects.all().order_by("-data_criacao")

    return render(request, "artigos/lista_artigos.html", {
        "artigos": artigos
    })