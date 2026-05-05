from django.contrib import admin
from .models import Artigo


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("autor", "data_criacao", "link_externo")
    search_fields = ("texto", "autor__username")
    list_filter = ("data_criacao", "autor")