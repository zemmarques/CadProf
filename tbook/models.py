from django.db import models
from django.core.urlresolvers import reverse
from datetime import date


class SchoolYear(models.Model):
    ''' um modelo para o ano letivo
    TODO - acrescentar duração dos períodos '''

    designation = models.CharField('Designação', max_length=200)
    slug = models.SlugField('Caminho')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    def get_absolute_url(self):
        return reverse('tbook:classes', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Ano Letivo'
        verbose_name_plural = 'Anos Letivos'
        ordering = ['designation']


class SchoolClass(models.Model):
    ''' um modelo para o registo das turmas'''

    YEAR_IN_SCHOOL_CHOICES = (
        ("7ºano", "7º Ano"), ("8ºano", "8º Ano"),
        ("9ºano", "9º Ano"), ("10ºano", "10º Ano"),
        ("11ºano", "11º Ano"), ("12ºano", "12º Ano"),
    )

    school_year = models.ForeignKey(
        'tbook.SchoolYear', verbose_name='Ano Letivo', on_delete=models.CASCADE
    )
    designation = models.CharField('Designação', max_length=50)
    slug = models.SlugField('Caminho')
    school = models.CharField('Escola', max_length=200)
    year_in_school = models.CharField(
        'Ano', choices=YEAR_IN_SCHOOL_CHOICES, max_length=100, default='7º Ano'
    )
    max_students = models.IntegerField('máx alunos', default=25)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    def get_absolute_url(self):
        ano_letivo = SchoolYear.objects.get(id=self.school_year.id)
        print(ano_letivo.slug)
        print(self.slug)
        return reverse('tbook:student', kwargs={
            'school_year_slug': ano_letivo.slug,
            'turma_slug': self.slug
            })

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['designation']


class Student(models.Model):
    ''' modelo para os alunos da turma'''

    school_class = models.ForeignKey(
        'tbook.SchoolClass', verbose_name='Turma', on_delete=models.CASCADE
    )
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Caminho')
    number = models.IntegerField('Número')
    birth_date = models.DateField('Data de Nascimento')
    email = models.EmailField('Email', max_length=254, unique=True)
    tutor = models.CharField('Enc.Educação', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    def get_age(self):
        ''' calculate age from actual date an birth_date'''
        today = date.today()
        return today.year - self.birth_date.year - \
            ((today.month, today.day) <
                (self.birth_date.month, self.birth_date.day))

    def get_first_name(self):
        return str(self).split(" ")[0]

    def get_last_name(self):
        return str(self).split(" ")[-1]

    def get_absolute_url(self):
        turma = SchoolClass.objects.get(id=self.school_class.id)
        ano_letivo = SchoolYear.objects.get(id=turma.school_year.id)
        return reverse('tbook:each_student', kwargs={
            'school_year_slug': ano_letivo.slug, 'turma_slug': turma.slug,
            'slug': self.slug
            })

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['school_class']


class School_Test(models.Model):
    ''' um modelo para os testes'''

    designation = models.CharField('Designação', max_length=50)
    subjects = models.TextField('Conteúdos', blank=True)
    notes = models.TextField('Observações', blank=True)
    date = models.DateField('data')
    slug = models.SlugField('Caminho')
    grade = models.DecimalField(
        'Classificação', decimal_places=2, max_digits=6
    )

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Teste'
        verbose_name_plural = 'Testes'
        ordering = ['created']


class Score(models.Model):
    ''' resumo dos testes da turma'''

    test = models.ForeignKey(
        'tbook.School_Test', verbose_name='Teste', on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        'tbook.Student', verbose_name='Aluno', on_delete=models.CASCADE
    )
    school_class = models.ForeignKey(
        'tbook.SchoolClass', verbose_name='Turma', on_delete=models.CASCADE
    )
