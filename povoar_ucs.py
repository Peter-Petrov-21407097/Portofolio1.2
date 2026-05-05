import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular


licenciatura = Licenciatura.objects.first()

ucs = [
    {
        "nome": "Matemática Discreta",
        "ano_curricular": 1,
        "semestre": 1,
        "ects": 6,
        "apresentacao": "Introdução aos conceitos fundamentais da matemática discreta, essenciais para a computação.",
        "programa": "Lógica proposicional. Teoria de conjuntos. Relações e funções. Combinatória. Grafos. Árvores.",
        "objectivos": "Dotar os alunos de ferramentas matemáticas para análise de algoritmos e estruturas computacionais.",
        "imagem": None,
        "url_website": "https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica/ULHT260-1656",
    },
    {
        "nome": "Arquitetura de Computadores",
        "ano_curricular": 1,
        "semestre": 2,
        "ects": 6,
        "apresentacao": "Estudo da organização interna dos computadores e dos seus componentes principais.",
        "programa": "Representação da informação. Sistemas digitais. CPU. Memória. Input/Output. Assembly básico.",
        "objectivos": "Compreender o funcionamento interno dos sistemas computacionais e a interação entre hardware e software.",
        "imagem": None,
        "url_website": "https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica/ULHT260-7",
    },
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