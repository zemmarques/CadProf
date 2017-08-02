from django.shortcuts import render
# from django.http import HttpResponse
from .models import SchoolYear, SchoolClass


def index(request):
    '''apresenta todos os registos de anos letivos na página inicial'''

    template_name = 'tbook/index.html'
    todos_anos_letivos = SchoolYear.objects.all()
    context = {
        'anos_letivos': todos_anos_letivos
    }
    return render(request, template_name, context)


def detail(request, school_year_id):
    ''' apresenta as turmas de um ano letivo '''

    template_name = 'tbook/turmas.html'
    turmas = SchoolClass.objects.filter(school_year_id=school_year_id)
    ano_letivo = SchoolYear.objects.get(id=school_year_id)
    print(ano_letivo)
    context = {
        'turmas': turmas,
        'id_AnoLetivo': ano_letivo
    }
    return render(request, template_name, context)
