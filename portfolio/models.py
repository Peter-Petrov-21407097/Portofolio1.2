from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    numero_semestres = models.PositiveIntegerField()
    ects_total = models.PositiveIntegerField()
    descricao = models.TextField()
    objetivo = models.TextField()
    url_website = models.URLField()
    saidas_profissionais = models.TextField()
    imagem = models.ImageField(upload_to='licenciaturas/', blank=True, null=True)

    def __str__(self):
        return self.nome
    
