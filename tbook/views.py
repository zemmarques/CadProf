from django.shortcuts import render
# from django.http import HttpResponse
from .models import SchoolYear, SchoolTerm, School, SchoolClass, Student


def index(request, **kargs):
    '''apresenta dados do ano letivo currente na página inicial se apenas
    for dado um argumento. Se forem passados dois argumentos apresenta o ano
    letivo selecionado'''

    if kargs:
        slug = kargs.get('slug')
        current_school_year = SchoolYear.objects.get(slug=slug)
    else:
        current_school_year = SchoolYear.objects.latest('created')

    template_name = 'tbook/index.html'
    side_bar_school_years = SchoolYear.objects.order_by('-id')[:3]
    school_terms = SchoolTerm.objects.filter(
        school_year=current_school_year
    ).order_by('designation')
    school_classes = SchoolClass.objects.filter(
        school_year=current_school_year
    )
    students = []
    school_classes_dict = {}
    total_students = 0
    for shc in school_classes:
        s = Student.objects.filter(school_class=shc)
        students.append(s)
        school_classes_dict.update({shc: s.count()})
        total_students = total_students + s.count()

    mail_students = 0
    for stds in students:
        for s in stds:
            if s.sex == 'M':
                mail_students += 1

    fem_students = total_students - mail_students

    context = {
        'current_school_year': current_school_year,
        'side_bar_school_years': side_bar_school_years,
        'school_terms': school_terms,
        'school_classes_dict': school_classes_dict,
        'students': students,
        'total_students': total_students,
        'mail_students': mail_students,
        'fem_students': fem_students,
    }
    return render(request, template_name, context)


def school_class_func(request, school_year_slug, school_class_slug):
    ''' apresenta os dados da turma selecionada'''

    template_name = 'tbook/school_class_page.html'
    school_class = SchoolClass.objects.get(slug=school_class_slug)

    current_school_year = SchoolYear.objects.get(slug=school_year_slug)
    side_bar_school_years = SchoolYear.objects.order_by('-id')[:3]
    school_terms = SchoolTerm.objects.filter(
        school_year=current_school_year
    ).order_by('designation')
    students = Student.objects.filter(school_class=school_class)
    total_students = students.count()
    school_classes_dict = SchoolClass.objects.filter(
        school_year=current_school_year
    )

    context = {
        'current_school_year': current_school_year,
        'side_bar_school_years': side_bar_school_years,
        'school_terms': school_terms,
        'school_class': school_class,
        'students': students,
        'total_students': total_students,
        'school_classes_dict': school_classes_dict,
    }
    return render(request, template_name, context)


def student_profile_func(request, school_year_slug, school_class_slug, slug):
    ''' apresenta a ficha completa de cada aluno'''

    template_name = 'tbook/student_profile.html'
    student = Student.objects.get(slug=slug)
    school_class = SchoolClass.objects.get(slug=school_class_slug)

    current_school_year = SchoolYear.objects.get(slug=school_year_slug)
    side_bar_school_years = SchoolYear.objects.order_by('-id')[:3]
    school_classes_dict = SchoolClass.objects.filter(
        school_year=current_school_year
    )

    context = {
        'current_school_year': current_school_year,
        'side_bar_school_years': side_bar_school_years,
        'school_class': school_class,
        'school_classes_dict': school_classes_dict,
        'student': student,
    }
    return render(request, template_name, context)


def all_school_years_func(request):
    ''' Apresenta todos os registos de anos letivos guardados na base de
    dados da aplicação'''

    template_name = 'tbook/all_school_years.html'
    all_school_years = SchoolYear.objects.all().order_by('-created')

    context = {
        'all_school_years': all_school_years,
    }
    return render(request, template_name, context)


def all_schools_func(request):
    ''' Apresenta todas as Escolas guardadas na base de dados do sistema'''

    template_name = 'tbook/all_schools.html'
    all_schools = School.objects.all().order_by('-created')
    side_bar_school_years = SchoolYear.objects.order_by('-id')[:3]

    context = {
        'all_schools': all_schools,
        'side_bar_school_years': side_bar_school_years,
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
