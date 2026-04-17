from django.shortcuts import render
from .models import (
    Licenciatura,
    UnidadeCurricular,
    Tecnologia,
    Competencia,
    Formacao,
    AreaInteresse,
    TFC,
    Projeto,
    MakingOf,
    Midia,
    Docente,
)


def home(request):
    contexto = {
        "licenciaturas": Licenciatura.objects.all(),
        "ucs": UnidadeCurricular.objects.all(),
        "tecnologias": Tecnologia.objects.all(),
        "competencias": Competencia.objects.all(),
        "formacoes": Formacao.objects.all().order_by("ordem_cronologica"),
        "areas_interesse": AreaInteresse.objects.all(),
        "tfcs": TFC.objects.all(),
        "projetos": Projeto.objects.all(),
        "makingofs": MakingOf.objects.all().order_by("-data_registo"),
        "midias": Midia.objects.all().order_by("-data_upload"),
        "docentes": Docente.objects.all(),
    }
    return render(request, "portfolio/home.html", contexto)