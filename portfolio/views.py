from django.shortcuts import render, get_object_or_404
from .models import (
    Licenciatura,
    UnidadeCurricular,
    Projeto,
    Tecnologia,
    TFC,
    Competencia,
    Formacao,
    MakingOf,
    Docente,
    AreaInteresse,
    Midia,
)


def build_detail_context(obj, title, fields, image_attr=None, related_sections=None):
    details = []

    for label, value in fields:
        if value is not None and value != "":
            details.append((label, value))

    image_url = None
    if image_attr:
        image_field = getattr(obj, image_attr, None)
        if image_field:
            try:
                image_url = image_field.url
            except Exception:
                image_url = None

    return {
        "page_title": title,
        "object_name": str(obj),
        "details": details,
        "image_url": image_url,
        "related_sections": related_sections or [],
    }


def licenciatura_detail(request, id):
    obj = get_object_or_404(Licenciatura, id=id)

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Licenciatura",
        image_attr="imagem",
        fields=[
            ("Nome", obj.nome),
            ("Número de semestres", obj.numero_semestres),
            ("ECTS total", obj.ects_total),
            ("Descrição", obj.descricao),
            ("Objetivo", obj.objetivo),
            ("Website", obj.url_website),
            ("Saídas profissionais", obj.saidas_profissionais),
        ],
        related_sections=[
            ("Unidades Curriculares", obj.unidades_curriculares.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def unidade_curricular_detail(request, id):
    obj = get_object_or_404(
        UnidadeCurricular.objects.select_related("licenciatura").prefetch_related("docentes", "projetos", "midias"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Unidade Curricular",
        image_attr="imagem",
        fields=[
            ("Nome", obj.nome),
            ("Licenciatura", obj.licenciatura),
            ("Ano curricular", obj.ano_curricular),
            ("Semestre", obj.semestre),
            ("ECTS", obj.ects),
            ("Apresentação", obj.apresentacao),
            ("Programa", obj.programa),
            ("Objetivos", obj.objectivos),
            ("Website", obj.url_website),
        ],
        related_sections=[
            ("Docentes", obj.docentes.all()),
            ("Projetos", obj.projetos.all()),
            ("Mídias", obj.midias.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def projeto_detail(request, id):
    obj = get_object_or_404(
        Projeto.objects.select_related("unidade_curricular", "area_interesse")
        .prefetch_related("tecnologias", "competencias", "makingofs", "midias"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe do Projeto",
        image_attr="imagem",
        fields=[
            ("Título", obj.titulo),
            ("Unidade Curricular", obj.unidade_curricular),
            ("Área de interesse", obj.area_interesse),
            ("Descrição", obj.descricao),
            ("Conceitos aplicados", obj.conceitos_aplicados),
            ("Ano de realização", obj.ano_realizacao),
            ("Estado", obj.estado),
            ("Destaque", "Sim" if obj.destaque else "Não"),
        ],
        related_sections=[
            ("Tecnologias", obj.tecnologias.all()),
            ("Competências", obj.competencias.all()),
            ("Making Of", obj.makingofs.all()),
            ("Mídias", obj.midias.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def tecnologia_detail(request, id):
    obj = get_object_or_404(
        Tecnologia.objects.prefetch_related("projetos", "formacoes", "tfcs", "makingofs", "midias"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Tecnologia",
        image_attr="logo",
        fields=[
            ("Nome", obj.nome),
            ("Tipo", obj.tipo),
            ("Descrição", obj.descricao),
            ("Website", obj.url_website),
            ("Observações", obj.observacoes),
        ],
        related_sections=[
            ("Projetos", obj.projetos.all()),
            ("Formações", obj.formacoes.all()),
            ("TFCs", obj.tfcs.all()),
            ("Making Of", obj.makingofs.all()),
            ("Mídias", obj.midias.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def tfc_detail(request, id):
    obj = get_object_or_404(
        TFC.objects.select_related("area_interesse")
        .prefetch_related("tecnologias", "makingofs"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe do TFC",
        image_attr="imagem",
        fields=[
            ("Título", obj.titulo),
            ("Autor", obj.autor),
            ("Orientador", obj.orientador),
            ("Curso", obj.curso),
            ("Ano", obj.ano),
            ("Resumo", obj.resumo),
            ("Palavras-chave", obj.palavras_chave),
            ("Email do autor", obj.email_autor),
            ("Documento", obj.documento_url),
            ("Classificação de interesse", obj.classificacao_interesse),
            ("Área de interesse", obj.area_interesse),
            ("Destaque", "Sim" if obj.destaque else "Não"),
        ],
        related_sections=[
            ("Tecnologias", obj.tecnologias.all()),
            ("Making Of", obj.makingofs.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def competencia_detail(request, id):
    obj = get_object_or_404(
        Competencia.objects.prefetch_related("projetos", "formacoes", "makingofs"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Competência",
        fields=[
            ("Nome", obj.nome),
            ("Tipo", obj.tipo),
            ("Descrição", obj.descricao),
            ("Nível", obj.nivel),
            ("Evidência", obj.evidencia),
            ("Destaque", "Sim" if obj.destaque else "Não"),
        ],
        related_sections=[
            ("Projetos", obj.projetos.all()),
            ("Formações", obj.formacoes.all()),
            ("Making Of", obj.makingofs.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def formacao_detail(request, id):
    obj = get_object_or_404(
        Formacao.objects.prefetch_related("competencias", "tecnologias", "makingofs"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Formação",
        fields=[
            ("Nome", obj.nome),
            ("Instituição", obj.instituicao),
            ("Tipo", obj.tipo),
            ("Data de início", obj.data_inicio),
            ("Data de fim", obj.data_fim),
            ("Descrição", obj.descricao),
            ("Certificado", obj.certificado_url),
            ("Estado", obj.estado),
            ("Ordem cronológica", obj.ordem_cronologica),
        ],
        related_sections=[
            ("Competências", obj.competencias.all()),
            ("Tecnologias", obj.tecnologias.all()),
            ("Making Of", obj.makingofs.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def makingof_detail(request, id):
    obj = get_object_or_404(
        MakingOf.objects.select_related(
            "projeto",
            "unidade_curricular",
            "tecnologia",
            "tfc",
            "formacao",
            "competencia",
        ).prefetch_related("midias"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe do Making Of",
        fields=[
            ("Título", obj.titulo),
            ("Descrição", obj.descricao),
            ("Data de registo", obj.data_registo),
            ("Versão do modelo", obj.versao_modelo),
            ("Decisões tomadas", obj.decisoes_tomadas),
            ("Erros encontrados", obj.erros_encontrados),
            ("Correções realizadas", obj.correcoes_realizadas),
            ("Justificação da modelação", obj.justificacao_modelacao),
            ("Uso de IA", obj.uso_ia),
            ("Observações", obj.observacoes),
            ("Projeto", obj.projeto),
            ("Unidade Curricular", obj.unidade_curricular),
            ("Tecnologia", obj.tecnologia),
            ("TFC", obj.tfc),
            ("Formação", obj.formacao),
            ("Competência", obj.competencia),
        ],
        related_sections=[
            ("Mídias", obj.midias.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def docente_detail(request, id):
    obj = get_object_or_404(
        Docente.objects.prefetch_related("unidades_curriculares"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe do Docente",
        image_attr="foto",
        fields=[
            ("Nome", obj.nome),
            ("Email", obj.email),
            ("Área de especialização", obj.area_especializacao),
            ("Página pessoal", obj.pagina_pessoal_url),
        ],
        related_sections=[
            ("Unidades Curriculares", obj.unidades_curriculares.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def area_interesse_detail(request, id):
    obj = get_object_or_404(
        AreaInteresse.objects.prefetch_related("projetos", "tfcs"),
        id=id,
    )

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Área de Interesse",
        fields=[
            ("Nome", obj.nome),
            ("Descrição", obj.descricao),
            ("Categoria", obj.categoria),
            ("Destaque", "Sim" if obj.destaque else "Não"),
        ],
        related_sections=[
            ("Projetos", obj.projetos.all()),
            ("TFCs", obj.tfcs.all()),
        ],
    )
    return render(request, "portfolio/detalhe.html", context)


def midia_detail(request, id):
    obj = get_object_or_404(
        Midia.objects.select_related("unidade_curricular", "projeto", "tecnologia", "making_of"),
        id=id,
    )

    file_url = None
    try:
        file_url = obj.ficheiro.url
    except Exception:
        file_url = None

    context = build_detail_context(
        obj=obj,
        title="Detalhe da Mídia",
        fields=[
            ("Título", obj.titulo),
            ("Tipo", obj.tipo),
            ("Legenda", obj.legenda),
            ("Descrição", obj.descricao),
            ("Data de upload", obj.data_upload),
            ("Unidade Curricular", obj.unidade_curricular),
            ("Projeto", obj.projeto),
            ("Tecnologia", obj.tecnologia),
            ("Making Of", obj.making_of),
            ("Ficheiro", file_url),
        ],
    )

    return render(request, "portfolio/detalhe.html", context)


def home_view(request):
    context = {
        "licenciaturas": Licenciatura.objects.all(),
        "ucs": UnidadeCurricular.objects.all(),
        "tecnologias": Tecnologia.objects.all(),
        "competencias": Competencia.objects.all(),
        "formacoes": Formacao.objects.all(),
        "areas_interesse": AreaInteresse.objects.all(),
        "tfcs": TFC.objects.all(),
        "projetos": Projeto.objects.all(),
        "makingofs": MakingOf.objects.all(),
        "midias": Midia.objects.all(),
        "docentes": Docente.objects.all(),
    }
    return render(request, "portfolio/home.html", context)
    return render(request, "portfolio/detalhe.html", context)