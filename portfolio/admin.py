from django.contrib import admin




@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_semestres', 'ects_total', 'url_website')
    search_fields = ('nome', 'descricao', 'objetivo')
    list_filter = ('numero_semestres', 'ects_total')

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'licenciatura', 'ano_curricular', 'semestre', 'ects', 'url_website')
    search_fields = ('nome', 'apresentacao', 'programa', 'objectivos')
    list_filter = ('licenciatura', 'ano_curricular', 'semestre', 'ects')    

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'area_especializacao', 'pagina_pessoal_url')
    search_fields = ('nome', 'email', 'area_especializacao')
    list_filter = ('area_especializacao',)
    filter_horizontal = ('unidades_curriculares',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'unidade_curricular', 'ano_realizacao', 'estado', 'destaque')
    search_fields = ('titulo', 'descricao', 'conceitos_aplicados')
    list_filter = ('unidade_curricular', 'ano_realizacao', 'estado', 'destaque')