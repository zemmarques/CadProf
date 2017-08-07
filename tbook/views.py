from django.shortcuts import render
# from django.http import HttpResponse
from .models import SchoolYear, SchoolClass, Student


def index(request):
    '''apresenta todos os registos de anos letivos na página inicial'''

    template_name = 'tbook/index.html'
    todos_anos_letivos = SchoolYear.objects.all()

    context = {
        'anos_letivos': todos_anos_letivos
    }
    return render(request, template_name, context)


def classes(request, slug):
    ''' apresenta as turmas de um ano letivo '''

    template_name = 'tbook/turmas.html'
    ano_letivo = SchoolYear.objects.get(slug=slug)
    turmas = SchoolClass.objects.filter(school_year=ano_letivo)

    context = {
        'turmas': turmas,
        'AnoLetivo': ano_letivo
    }
    return render(request, template_name, context)


def alunos(request, school_year_slug, turma_slug):
    template_name = 'tbook/alunos.html'
    ano_letivo = SchoolYear.objects.get(slug=school_year_slug)
    turma = SchoolClass.objects.get(slug=turma_slug)
    alunos = Student.objects.filter(school_class=turma)

    context = {
        'ano_letivo': ano_letivo,
        'turma': turma,
        'alunos': alunos
    }
    return render(request, template_name, context)


def aluno(request, school_year_slug, turma_slug, slug):
    template_name = 'tbook/aluno.html'
    ano_letivo = SchoolYear.objects.get(slug=school_year_slug)
    turma = SchoolClass.objects.get(slug=turma_slug)
    aluno = Student.objects.get(slug=slug)

    context = {
        'ano_letivo': ano_letivo,
        'turma': turma,
        'aluno': aluno
    }
    return render(request, template_name, context)
