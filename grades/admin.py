from django.contrib import admin
from grades.models import (SchoolTest, Question,)


class SchoolTestAdmin(admin.ModelAdmin):
    ''' Criação da tabela do teste'''

    prepopulated_fields = {'slug': ('designation',), }

    list_display = [
        'designation', 'get_subject', 'get_school_term', 'get_student',
        'grade', 'date', 'contents', 'created', 'modified'
    ]
    search_fields = [
        'designation', 'get_subject', 'get_school_term', 'get_student',
        'grade', 'date', 'contents', 'created', 'modified'
    ]

    list_filter = [
        'designation', 'subject', 'school_term', 'student', 'grade', 'date',
        'contents', 'created', 'modified'
    ]

    def get_subject(self, obj):
        return obj.subject.designation

    # Allows column order sorting
    get_subject.admin_order_field = 'subject'
    # Renames column head
    get_subject.short_description = 'Disciplina'

    def get_school_term(self, obj):
        return obj.school_term.designation

    # Allows column order sorting
    get_school_term.admin_order_field = 'school_term'
    # Renames column head
    get_school_term.short_description = 'Período'

    def get_student(self, obj):
        return obj.student.name

    # Allows column order sorting
    get_student.admin_order_field = 'student'
    # Renames column head
    get_student.short_description = 'Aluno'

admin.site.register(SchoolTest, SchoolTestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    ''' tabela de questões no admin'''

    prepopulated_fields = {'slug': ('designation',), }

    list_display = [
        'designation', 'cotation', 'value', 'get_school_test', 'created',
        'modified'
    ]
    search_fields = [
        'designation', 'cotation', 'value', 'get_school_test', 'created',
        'modified'
    ]

    list_filter = [
        'designation', 'cotation', 'value', 'school_test', 'created',
        'modified'
    ]

    def get_school_test(self, obj):
        return obj.school_test.designation

    # Allows column order sorting
    get_school_test.admin_order_field = 'school_test'
    # Renames column head
    get_school_test.short_description = 'Teste'

admin.site.register(Question, QuestionAdmin)
