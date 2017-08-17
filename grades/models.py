from django.db import models
from django.core.urlresolvers import reverse


class SchoolTest(models.Model):
    ''' um modelo para os testes'''

    student = models.ForeignKey(
        'tbook.Student', verbose_name='Aluno', on_delete=models.CASCADE
    )

    school_class = models.ForeignKey(
        'tbook.SchoolClass', verbose_name='Turma', blank=True,
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        'tbook.Subject', verbose_name='Disciplina', on_delete=models.CASCADE
    )
    school_term = models.ForeignKey(
        'tbook.SchoolTerm', verbose_name='Período', on_delete=models.CASCADE
    )
    designation = models.CharField('Designação', max_length=50)
    grade = models.DecimalField(
        'Classificação', decimal_places=2, max_digits=6, null=True, blank=True
    )
    date = models.DateField('data')
    contents = models.TextField('Conteúdos', blank=True)
    notes = models.TextField('Observações', blank=True)

    slug = models.SlugField('Caminho')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Teste'
        verbose_name_plural = 'Testes'
        ordering = ['created']


class Question(models.Model):
    ''' um modelo para as questões dos testes'''

    school_test = models.ForeignKey(
        'grades.SchoolTest', verbose_name='Teste', on_delete=models.CASCADE
    )
    designation = models.CharField('Designação', max_length=50)
    cotation = models.DecimalField(
        'Cotação', decimal_places=2, max_digits=6, null=True, blank=True
    )
    value = models.DecimalField(
        'Nota', decimal_places=2, max_digits=6, null=True, blank=True
    )

    slug = models.SlugField('Caminho')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ['created']
