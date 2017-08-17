from django.contrib import admin
from tbook.models import(
    SchoolYear, SchoolTerm, School, Subject, SchoolClass, Student,)


class SchoolYearAdmin(admin.ModelAdmin):
    """ Definições para entradas de Anos Letivos no Admin"""

    prepopulated_fields = {'slug': ('designation',), }

    list_display = ['designation', 'created', 'modified']
    search_fields = ['designation', 'created', 'modified']

    list_filter = ['designation', 'created', 'modified']

admin.site.register(SchoolYear, SchoolYearAdmin)


class SchoolTermAdmin(admin.ModelAdmin):
    ''' tabela dos períodos letivos no admin'''

    prepopulated_fields = {'slug': ('designation',), }

    list_display = [
        'designation', 'start_date', 'end_date', 'get_school_year', 'created',
        'modified'
    ]
    search_fields = [
        'designation', 'start_date', 'end_date', 'get_school_year', 'created',
        'modified'
    ]
    list_filter = [
        'designation', 'start_date', 'end_date', 'school_year', 'created',
        'modified'
    ]

    def get_school_year(self, obj):
        return obj.school_year.designation

    # Allows column order sorting
    get_school_year.admin_order_field = 'school_year'
    # Renames column head
    get_school_year.short_description = 'Ano Letivo'

admin.site.register(SchoolTerm, SchoolTermAdmin)


class SchoolAdmin(admin.ModelAdmin):
    ''' tabela das escolas no admin'''

    prepopulated_fields = {'slug': ('name',), }

    list_display = ['name', 'code', 'adress', 'phone', 'created', 'modified']
    search_fields = ['name', 'code', 'adress', 'phone', 'created', 'modified']
    list_filter = ['name', 'code', 'adress', 'phone', 'created', 'modified']

admin.site.register(School, SchoolAdmin)


class SubjectAdmin(admin.ModelAdmin):
    ''' Apresentação de disiciplinas no Admin'''

    prepopulated_fields = {'slug': ('sigla',), }

    list_display = ['designation', 'sigla', 'created', 'modified']
    search_fields = ['designation', 'sigla', 'created', 'modified']
    list_filter = ['designation', 'sigla', 'created', 'modified']

admin.site.register(Subject, SubjectAdmin)


class SchoolClassAdmin(admin.ModelAdmin):
    ''' Criação da Tabela do turma '''

    prepopulated_fields = {'slug': ('designation',), }

    list_display = [
        'designation', 'get_subject', 'get_school', 'year_in_school',
        'get_school_year'
    ]
    search_fields = [
        'designation', 'get_subject', 'get_school', 'year_in_school',
        'get_school_year'
    ]
    list_filter = [
        'designation', 'subject', 'school', 'year_in_school', 'school_year'
    ]

    def get_school_year(self, obj):
        return obj.school_year.designation

    # Allows column order sorting
    get_school_year.admin_order_field = 'school_year'
    # Renames column head
    get_school_year.short_description = 'Ano Letivo'

    def get_school(self, obj):
        return obj.school.name

    # Allows column order sorting
    get_school.admin_order_field = 'school'
    # Renames column head
    get_school.short_description = 'Escola'

    def get_subject(self, obj):
        return obj.subject.designation

    # Allows column order sorting
    get_subject.admin_order_field = 'subject'
    # Renames column head
    get_subject.short_description = 'Disciplina'

admin.site.register(SchoolClass, SchoolClassAdmin)


class StudentAdmin(admin.ModelAdmin):
    ''' Criação da Tabela do aluno '''

    prepopulated_fields = {'slug': ('name', 'school_class', ), }

    list_display = [
        'name', 'get_school_class', 'number', 'birth_date', 'tutor'
    ]
    search_fields = [
        'name', 'get_school_class', 'number', 'birth_date', 'tutor'
    ]
    list_filter = ['name', 'number', 'school_class', 'birth_date', 'tutor']

    def get_school_class(self, obj):
        return obj.school_class.designation

    # Allows column order sorting
    get_school_class.admin_order_field = 'school_class'
    # Renames column head
    get_school_class.short_description = 'Turma'

admin.site.register(Student, StudentAdmin)


# class ScoreAdmin(admin.ModelAdmin):
#     ''' registos de testes'''
#
#     list_display = ['get_test', 'get_school_class', 'get_student']
#     search_fields = ['get_test', 'get_school_class', 'get_student']
#     list_filter = ['test', 'school_class', 'student']
#
#     def get_test(self, obj):
#         return obj.test.designation
#
#     def get_school_class(self, obj):
#         return obj.school_class.designation
#
#     def get_student(self, obj):
#         return obj.student.name
#
#
# admin.site.register(Score, ScoreAdmin)
