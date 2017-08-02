from django.db import models


class SchoolYear(models.Model):
    ''' um modelo para o ano letivo
    TODO - acrescentar duração dos períodos '''

    designation = models.CharField('Designação', max_length=200)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

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
    school = models.CharField('Escola', max_length=200)
    year_in_school = models.CharField(
        'Ano', choices=YEAR_IN_SCHOOL_CHOICES, max_length=100, default='7º Ano'
    )
    max_students = models.IntegerField('máx alunos', default=25)

    def __str__(self):
        return self.designation

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
    number = models.IntegerField('Número')
    birth_date = models.DateField('Data de Nascimento')
    tutor = models.CharField('Enc.Educação', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['school_class']
