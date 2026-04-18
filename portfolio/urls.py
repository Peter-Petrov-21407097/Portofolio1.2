from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("licenciaturas/", views.lista_licenciaturas, name="lista_licenciaturas"),
    path("ucs/", views.lista_ucs, name="lista_ucs"),
    path("tecnologias/", views.lista_tecnologias, name="lista_tecnologias"),
    path("competencias/", views.lista_competencias, name="lista_competencias"),
    path("formacoes/", views.lista_formacoes, name="lista_formacoes"),
    path("areas/", views.lista_areas_interesse, name="lista_areas_interesse"),
    path("tfcs/", views.lista_tfcs, name="lista_tfcs"),
    path("projetos/", views.lista_projetos, name="lista_projetos"),
    path("makingof/", views.lista_makingof, name="lista_makingof"),
    path("midias/", views.lista_midias, name="lista_midias"),
    path("docentes/", views.lista_docentes, name="lista_docentes"),
]