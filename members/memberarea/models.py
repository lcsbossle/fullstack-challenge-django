from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

# class User(AbstractUser):
#     PROFESSOR = 1
#     ALUNO = 2
# 
#     ROLE_CHOICES = (
#         (PROFESSOR, 'Professor'),
#         (ALUNO, 'Aluno'),
#     )
# 
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class Aula(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(max_length=500)
    conteudo = models.TextField(max_length=50000)
    
    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Aulas'
    
    def __str__(self):
        return self.titulo
    
class Curso(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(max_length=500)
    aulas = models.ManyToManyField(
        Aula,
        through='Sequencia',
        through_fields=('curso','aula'),
    )
    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return self.titulo
    
class Sequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    sequencia = models.IntegerField(null=True)
    
    class Meta:
        unique_together = ['curso', 'aula']







