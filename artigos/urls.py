from django.urls import path
from . import views

app_name = "artigos"

urlpatterns = [
    path("", views.lista_artigos, name="lista_artigos"),
    path("criar/", views.criar_artigo, name="criar_artigo"),
    path("<int:id>/editar/", views.editar_artigo, name="editar_artigo"),
    path("<int:id>/like/", views.like_artigo, name="like_artigo"),
    path("<int:id>/comentar/", views.comentar_artigo, name="comentar_artigo"),
]