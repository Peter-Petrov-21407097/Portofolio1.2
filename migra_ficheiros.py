import os

from django.core.files import File

from portfolio.models import (
    Licenciatura,
    UnidadeCurricular,
    Tecnologia,
    TFC,
    Projeto,
    Midia,
    Docente,
)

BASE_MEDIA = "media"


def migrar(modelo, campo_nome):
    for obj in modelo.objects.all():

        campo = getattr(obj, campo_nome)

        if campo and campo.name:

            local_path = os.path.join(BASE_MEDIA, campo.name)

            if os.path.exists(local_path):

                with open(local_path, 'rb') as f:

                    campo.save(
                        os.path.basename(local_path),
                        File(f),
                        save=True
                    )

                print(f"Migrado: {obj}")

            else:
                print(f"Ficheiro não encontrado: {local_path}")


migrar(Licenciatura, 'imagem')
migrar(UnidadeCurricular, 'imagem')
migrar(Tecnologia, 'logo')
migrar(TFC, 'imagem')
migrar(Projeto, 'imagem')
migrar(Midia, 'ficheiro')
migrar(Docente, 'foto')

print("Migração concluída.")