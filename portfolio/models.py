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


class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='unidades_curriculares'
    )
    nome = models.CharField(max_length=200)
    ano_curricular = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()
    ects = models.PositiveIntegerField()
    apresentacao = models.TextField()
    programa = models.TextField()
    objectivos = models.TextField()
    imagem = models.ImageField(upload_to='unidades_curriculares/', blank=True, null=True)
    url_website = models.URLField()

    def __str__(self):
        return self.nome
    
class Docente(models.Model):
    nome = models.CharField(max_length=200)
    pagina_pessoal_url = models.URLField()
    email = models.EmailField()
    area_especializacao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)
    unidades_curriculares = models.ManyToManyField(
        UnidadeCurricular,
        related_name='docentes',
        blank=True
    )

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name='projetos'
    )
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    ano_realizacao = models.PositiveIntegerField()
    estado = models.CharField(max_length=100)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    url_website = models.URLField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome    