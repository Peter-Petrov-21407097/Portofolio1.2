from django.contrib import admin


from .models import Licenciatura


@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_semestres', 'ects_total', 'url_website')
    search_fields = ('nome', 'descricao', 'objetivo')
    list_filter = ('numero_semestres', 'ects_total')