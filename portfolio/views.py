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
    return render(request, "portfolio/home.html")

def lista_licenciaturas(request):
    dados = Licenciatura.objects.all()
    return render(request, "portfolio/licenciaturas.html", {"dados": dados})

def lista_ucs(request):
    dados = UnidadeCurricular.objects.all()
    return render(request, "portfolio/ucs.html", {"dados": dados})

def lista_tecnologias(request):
    dados = Tecnologia.objects.all()
    return render(request, "portfolio/tecnologias.html", {"dados": dados})

def lista_competencias(request):
    dados = Competencia.objects.all()
    return render(request, "portfolio/competencias.html", {"dados": dados})

def lista_formacoes(request):
    dados = Formacao.objects.all()
    return render(request, "portfolio/formacoes.html", {"dados": dados})

def lista_areas_interesse(request):
    dados = AreaInteresse.objects.all()
    return render(request, "portfolio/areas.html", {"dados": dados})

def lista_tfcs(request):
    dados = TFC.objects.all()
    return render(request, "portfolio/tfcs.html", {"dados": dados})

def lista_projetos(request):
    dados = Projeto.objects.all()
    return render(request, "portfolio/projetos.html", {"dados": dados})

def lista_makingof(request):
    dados = MakingOf.objects.all()
    return render(request, "portfolio/makingof.html", {"dados": dados})

def lista_midias(request):
    dados = Midia.objects.all()
    return render(request, "portfolio/midias.html", {"dados": dados})

def lista_docentes(request):
    dados = Docente.objects.all()
    return render(request, "portfolio/docentes.html", {"dados": dados})