import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular


licenciatura = Licenciatura.objects.first()

ucs = [
    {
        "nome": "Fundamentos de Programação",
        "ano_curricular": 1,
        "semestre": 1,
        "ects": 6,
        "apresentacao": "Esta é uma disciplina fundamental na formação de qualquer profissional da área de Informática pois introduz os conceitos básicos da programação.",
        "programa": "Introdução à programação. Algoritmos, fluxogramas, pseudo-código. Sintaxe e semântica das linguagens. Tipos primitivos. Expressões. Entradas e saídas de dados. Seleção. Repetição. Funções. Arrays. Tratamento de erros. Leitura e escrita de ficheiros.",
        "objectivos": "Fornecer aos futuros profissionais da área da informática as bases para iniciarem a atividade de programação de modo disciplinado.",
        "imagem": None,
        "url_website": "https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica/ULHT260-7337",
    }
]

for uc in ucs:
    UnidadeCurricular.objects.update_or_create(
        nome=uc["nome"],
        defaults={
            "licenciatura": licenciatura,
            "ano_curricular": uc["ano_curricular"],
            "semestre": uc["semestre"],
            "ects": uc["ects"],
            "apresentacao": uc["apresentacao"],
            "programa": uc["programa"],
            "objectivos": uc["objectivos"],
            "url_website": uc["url_website"],
        }
    )

print("Unidades curriculares inseridas/atualizadas com sucesso.")