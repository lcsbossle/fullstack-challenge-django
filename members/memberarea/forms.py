from django.forms import ModelForm, ValidationError, CharField, ModelMultipleChoiceField, widgets
from . import models
import datetime as dt

class CursoForm(ModelForm):
    class Meta:
        model = models.Curso
        aulas = ModelMultipleChoiceField(queryset = models.Aula.objects.all())
        exclude = []
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'aulas': 'Aulas',
        }
    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
    
    def save(self):
        cur = self.instance
        if not cur:
            cur = models.Curso(
                titulo = self.titulo,
                descricao = self.descricao,
                aulas = self.aulas,
            )
        cur = cur.save()
        return cur
        
    

class AulaForm(ModelForm):
    class Meta:
        model = models.Aula
        exclude = []
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'conteudo': 'Conteúdo',
        }
        
    def __init__(self, *args, **kwargs):
        super(AulaForm, self).__init__(*args, **kwargs)
        
    def save(self):
        aul = self.instance
        if not aul:
            aul = models.Aula(
                titulo = self.titulo,
                descricao = self.descricao,
                conteudo = self.conteudo,
            )
        new_aula = aul
        aul = aul.save()
        return new_aula











