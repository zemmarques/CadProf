from django.contrib import admin
from tbook.models import SchoolYear, SchoolClass, Student


class SchoolYearAdmin(admin.ModelAdmin):
    """ Definições para entradas de Anos Letivos no Admin"""

    list_display = ['designation', 'created', 'modified']
    search_fields = ['designation', 'created', 'modified']
    # prepopulated_fields = {'slug': ('designa',)}
    list_filter = ['designation', 'created', 'modified']

admin.site.register(SchoolYear, SchoolYearAdmin)


class SchoolClassAdmin(admin.ModelAdmin):
    ''' Criação da Tabela do turma '''

    list_display = ['designation', 'school', 'year_in_school', 'get_name']
    search_fields = ['designation', 'school', 'year_in_school', 'get_name']
    list_filter = ['designation', 'school', 'year_in_school', 'school_year']

    def get_name(self, obj):
        return obj.school_year.designation

    get_name.admin_order_field = 'school_year'  # Allows column order sorting
    get_name.short_description = 'Ano Letivo'  # Renames column head

admin.site.register(SchoolClass, SchoolClassAdmin)


class StudentAdmin(admin.ModelAdmin):
    ''' Criação da Tabela do aluno '''

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
