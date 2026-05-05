from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artigo
from .forms import ArtigoForm, ComentarioForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name="autores").exists()


def lista_artigos(request):
    artigos = Artigo.objects.all().order_by("-data_criacao")

    return render(request, "artigos/lista_artigos.html", {
        "artigos": artigos,
        "is_autor": is_autor(request.user),
        "comentario_form": ComentarioForm(),
    })


@login_required
def criar_artigo(request):
    if not is_autor(request.user):
        return redirect("artigos:lista_artigos")

    form = ArtigoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user
        artigo.save()
        return redirect("artigos:lista_artigos")

    return render(request, "artigos/artigo_form.html", {
        "form": form,
        "is_autor": is_autor(request.user),
    })


@login_required
def editar_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if not is_autor(request.user) or artigo.autor != request.user:
        return redirect("artigos:lista_artigos")

    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)

    if form.is_valid():
        form.save()
        return redirect("artigos:lista_artigos")

    return render(request, "artigos/artigo_form.html", {
        "form": form,
        "is_autor": is_autor(request.user),
    })


def like_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if request.user.is_authenticated:
        if request.user in artigo.likes.all():
            artigo.likes.remove(request.user)
        else:
            artigo.likes.add(request.user)

    return redirect("artigos:lista_artigos")


@login_required
def comentar_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if request.method == "POST":
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()

    return redirect("artigos:lista_artigos")