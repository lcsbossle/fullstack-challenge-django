from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required
from . import models, forms

def home(request):
    data = {}
    template = 'members/cursos.html'
    cursos = models.Curso.objects.all()
    
    data['cursos'] = cursos
    
    return render(request, template, data)

@login_required
@permission_required('memberarea.view_aula')
def aula(request, a_id):
    data = {}
    template = 'members/ver_aula.html'
    
    aula = models.Aula.objects.get(pk = a_id)
    cursos = models.Curso.objects.all()
    
    data['aula'] = aula
    data['cursos'] = cursos
    
    return render(request, template, data)

@login_required
@permission_required('memberarea.add_aula')
def add_aula(request):
    data = {}
    template = 'members/add_aula.html'
    form = forms.AulaForm(request.POST or None)
    cursos = models.Curso.objects.all()
    
    if request.method == 'POST':
        if form.is_valid():
            aula = form.save()
            return redirect('aula', a_id = aula.pk)
            messages.success(request, 'Aula cadastrada com sucesso!')
        else:
            messages.error(request, 'Erro ao cadastrar aula.')
    
    data['form'] = form
    data['cursos'] = cursos
    
    return render(request, template, data)

@login_required
@permission_required('memberarea.change_aula')
def edit_aula(request, a_id):
    data = {}
    template = 'members/edit_aula.html'
    cursos = models.Curso.objects.all()
    aula = models.Aula.objects.get(pk = a_id)
    
    if request.method == 'GET':
        form = forms.AulaForm(instance=aula)
    elif request.method ==  'POST':
        form = forms.AulaForm(request.POST, instance=aula)
        
        if form.is_valid():
            aula = form.save()
            return redirect('aula', a_id = aula.pk)
        
    
    data['form'] = form
    data['aula'] = aula
    data['cursos'] = cursos
    
    return render(request,template, data)

@login_required
@permission_required('memberarea.delete_aula')
def del_aula(request, a_id):
    data = {}
    template = 'members/del_aula.html'
    aula = get_object_or_404(models.Aula, id=a_id)
    cursos = models.Curso.objects.all()
    
    if request.method == "POST":
        aula.delete()
        return redirect('home')
    
    data['aula'] = aula
    data['cursos'] = cursos
    
    return render(request, template, data)

def curso(request, c_id):
    data = {}
    template = 'members/ver_curso.html'
    
    sequencia = models.Sequencia.objects.filter(curso=c_id).order_by('sequencia')
    cursos = models.Curso.objects.all()
    curso = models.Curso.objects.get(pk = c_id)
    
    data['sequencia'] = sequencia
    data['cursos'] = cursos
    data['curso'] = curso
    
    return render(request, template, data)

@login_required
@permission_required('memberarea.add_curso')
def add_curso(request):
    data = {}
    template = 'members/add_curso.html'
    form = forms.CursoForm(request.POST or None)
    cursos = models.Curso.objects.all()
    
    if request.method == 'POST':
        if form.is_valid():
            curso = form.save()
            aulas_selected = list(map(int, request.POST.getlist('aulas')))
            titulo = request.POST.get('titulo')
            seq = 1
            
            for a in aulas_selected:
                curso = models.Curso.objects.filter(titulo = titulo).get()
                aula = models.Aula.objects.get(pk=a)
                sequencia_add = models.Sequencia.objects.create(
                    aula = aula,
                    curso = curso,
                    sequencia = seq)
                seq += 1
            
            return redirect('home')
        else:
            messages.error(request, 'Erro ao cadastrar curso.')
    
    data['form'] = form
    data['cursos'] = cursos
    
    return render(request, template, data)

@login_required
@permission_required('memberarea.change_curso')
def edit_curso(request, c_id):
    data = {}
    template = 'members/edit_curso.html'
    cursos = models.Curso.objects.all()
    curso = models.Curso.objects.get(pk = c_id)
    aulas_curso = list(models.Sequencia.objects.filter(curso=curso).values_list('aula', flat=True))        
    seq_curso = list(models.Sequencia.objects.filter(curso=curso).values_list('sequencia', flat=True))
    if not seq_curso:
        seq_curso = [1]

    if request.method == 'GET':
        form = forms.CursoForm(instance=curso)
    elif request.method == 'POST':
        form = forms.CursoForm(request.POST, instance=curso)
        
        if form.is_valid():
            form.save()
            
            aulas_selected = list(map(int, request.POST.getlist('aulas')))
            aulas_add = [a for a in aulas_selected if a not in aulas_curso]
            aulas_delete = [a for a in aulas_curso if a not in aulas_selected]
            
            for a in aulas_add:
                aula = models.Aula.objects.get(pk=a)
                if not seq_curso:
                    seq = 1
                else:
                    seq = max(seq_curso) + 1
                sequencia_add = models.Sequencia.objects.create(
                    aula = aula,
                    curso = curso,
                    sequencia = seq )
                seq_curso.append(seq)
                aulas_curso.append(a)
                
            
            for a in aulas_delete:
                aula = models.Aula.objects.get(pk=a)
                sequencia_del = models.Sequencia.objects.filter(aula=aula, curso=curso).delete()
            
            return redirect('curso', c_id=c_id)
    
    data['form'] = form
    data['curso'] = curso
    data['cursos'] = cursos
    
    return render(request, template, data)

@login_required
@permission_required('memberarea.delete_curso')
def del_curso(request, c_id):
    data = {}
    template = 'members/del_curso.html'
    curso = get_object_or_404(models.Curso, id=c_id)
    cursos = models.Curso.objects.all()
    if request.method == "POST":
        curso.delete()
        return redirect('home')
    
    data['curso'] = curso
    data['cursos'] = cursos
    
    return render(request, template, data)

def cursos(request):
    data = {}
    template = 'members/cursos.html'
    cursos = models.Curso.objects.all()
    
    data['cursos'] = cursos
    
    return render(request, template, data)



