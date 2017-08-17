from django.db import models
from django.core.urlresolvers import reverse
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


class SchoolYear(models.Model):
    ''' um modelo para o ano letivo'''

    designation = models.CharField('Designação', max_length=200)

    slug = models.SlugField('Caminho')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    def get_absolute_url(self):
        return reverse('tbook:index1', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Ano Letivo'
        verbose_name_plural = 'Anos Letivos'
        ordering = ['designation']


class SchoolTerm(models.Model):
    ''' um modelo para o período escolar'''

    DESIGNATION_CHOICES = (
        ("1º Período", "1º Período"), ("2º Período", "2º Período"),
        ("3º Período", "3º Período"),
    )

    designation = models.CharField(
        'Designação', choices=DESIGNATION_CHOICES, max_length=100,
        default='1ºPeríodo'
    )
    start_date = models.DateField('Início')
    end_date = models.DateField('Fim')
    school_year = models.ForeignKey(
        'tbook.SchoolYear', verbose_name='Ano Letivo', on_delete=models.CASCADE
    )

    slug = models.SlugField('Caminho')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
        ordering = ['start_date']


class School(models.Model):
    ''' Um modelo para a escola'''

    name = models.CharField('Designação', max_length=200)
    code = models.IntegerField('Código da Escola', blank=True)
    adress = models.TextField('Morada', blank=True)
    phone = PhoneNumberField(blank=True)
    admin_email = models.EmailField(
        'Email Direção', max_length=254, unique=True, blank=True
    )
    sevices_email = models.EmailField(
        'Email Secretaria', max_length=254, unique=True, blank=True
    )
    slug = models.SlugField('Caminho')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
        ordering = ['name']


class Subject(models.Model):
    ''' um modelo para a disciplina'''

    DESIGNATION_CHOICES = (
        ("Matemática", "Matemática"), ("Física", "Física"),
        ("Química", "Química"), ('Físico-Química', 'Físico-Química'),
        ("Outra", "Outra"),
    )
    SIGLA_CHOICES = (
        ("Mat", "Mat"), ("Fis", "Fis"), ("Quim", "Quim"), ("FQ", "FQ"),
        ("Outra", "Outra"),
    )

    designation = models.CharField(
        'Designação', choices=DESIGNATION_CHOICES, max_length=100,
        default='Física'
    )
    sigla = models.CharField(
        'Nome Curto', choices=SIGLA_CHOICES, max_length=100, default='Fis'
    )
    slug = models.SlugField('Caminho')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
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
    school = models.ForeignKey(
        'tbook.School', verbose_name='Escola', on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        'tbook.Subject', verbose_name='Disciplina', on_delete=models.CASCADE
    )
    designation = models.CharField('Designação', max_length=50)
    slug = models.SlugField('Caminho')
    year_in_school = models.CharField(
        'Ano', choices=YEAR_IN_SCHOOL_CHOICES, max_length=100, default='7º Ano'
    )
    max_students = models.IntegerField('máx alunos', default=25)
    teacher_in_charge = models.CharField(
        'Diretor de Turma', max_length=100, blank=True
    )
    tc_email = models.EmailField(
        'Email DT', max_length=254, unique=True, blank=True
    )

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    def get_absolute_url(self):
        ano_letivo = SchoolYear.objects.get(id=self.school_year.id)
        return reverse('tbook:schoolclass', kwargs={
            'school_year_slug': ano_letivo.slug,
            'school_class_slug': self.slug
            })

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['designation']


class Student(models.Model):
    ''' modelo para os alunos da turma'''

    SEX_CHOICES = (("M", "Masculino"), ("F", "Feminino"),)

    school_class = models.ForeignKey(
        'tbook.SchoolClass', verbose_name='Turma', on_delete=models.CASCADE
    )
    name = models.CharField('Nome', max_length=100)
    birth_date = models.DateField('Data de Nascimento')
    sex = models.CharField(
        'sexo', choices=SEX_CHOICES, max_length=100, default='7º Ano'
    )
    email = models.EmailField('Email', max_length=254, unique=True)
    phone = PhoneNumberField('Telefone', blank=True)
    adress = models.TextField('Morada', blank=True)
    number = models.IntegerField('Número na turma')
    foto = models.ImageField(
        'Foto', upload_to='media/fotos_alunos/',
        default='media/fotos_alunos/no-img.jpg'
    )
    nee = models.BooleanField('NEE', default=False)
    notes = models.TextField('Observações', blank=True)

    tutor = models.CharField('Enc.Educação', max_length=100)
    t_email = models.EmailField(
        'Email EE', max_length=254, unique=True, blank=True
    )
    t_phone = PhoneNumberField('Telefone EE', blank=True)

    slug = models.SlugField('Caminho')

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
        return reverse('tbook:student', kwargs={
            'school_year_slug': ano_letivo.slug,
            'school_class_slug': turma.slug,
            'slug': self.slug
        })

    # ver o site seguinte para tentar por a funcionar
    # as imagens formatadas no tamanho:
    # https://github.com/vinyll/django-imagefit

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['school_class']
