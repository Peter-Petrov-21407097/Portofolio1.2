from django.contrib import admin
from .models import (
    Licenciatura,
    UnidadeCurricular,
    Docente,
    Projeto,
    Tecnologia,
    Competencia,
    Formacao,
    AreaInteresse,
    TFC,
    MakingOf,
    Midia,
)


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


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'url_website')
    search_fields = ('nome', 'tipo', 'descricao', 'observacoes')
    list_filter = ('tipo',)


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel', 'destaque')
    search_fields = ('nome', 'tipo', 'descricao', 'evidencia')
    list_filter = ('tipo', 'nivel', 'destaque')


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'tipo', 'data_inicio', 'data_fim', 'estado', 'ordem_cronologica')
    search_fields = ('nome', 'instituicao', 'tipo', 'descricao')
    list_filter = ('tipo', 'estado')
    filter_horizontal = ('competencias', 'tecnologias')


@admin.register(AreaInteresse)
class AreaInteresseAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'destaque')
    search_fields = ('nome', 'descricao', 'categoria')
    list_filter = ('categoria', 'destaque')


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'orientador', 'curso', 'ano', 'area_interesse', 'classificacao_interesse', 'destaque')
    search_fields = ('titulo', 'autor', 'orientador', 'curso', 'resumo', 'palavras_chave', 'email_autor')
    list_filter = ('ano', 'curso', 'area_interesse', 'classificacao_interesse', 'destaque')
    filter_horizontal = ('tecnologias',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'unidade_curricular', 'area_interesse', 'ano_realizacao', 'estado', 'destaque')
    search_fields = ('titulo', 'descricao', 'conceitos_aplicados')
    list_filter = ('unidade_curricular', 'area_interesse', 'ano_realizacao', 'estado', 'destaque')
    filter_horizontal = ('tecnologias', 'competencias')


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_registo', 'versao_modelo')
    search_fields = (
        'titulo',
        'descricao',
        'decisoes_tomadas',
        'erros_encontrados',
        'correcoes_realizadas',
        'justificacao_modelacao',
        'uso_ia',
        'observacoes',
    )
    list_filter = ('data_registo', 'versao_modelo')


@admin.register(Midia)
class MidiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'data_upload')
    search_fields = ('titulo', 'tipo', 'legenda', 'descricao')
    list_filter = ('tipo', 'data_upload')