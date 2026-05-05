from django.db import models
from django.contrib.auth.models import User


class Artigo(models.Model):
    texto = models.TextField()
    fotografia = models.ImageField(upload_to="artigos/", blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="artigos_gostados", blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Artigo de {self.autor.username}"


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username}"