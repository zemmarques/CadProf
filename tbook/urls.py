from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w_-]+)/$', views.classes, name='classes'),
    url(
        r'^(?P<school_year_slug>[\w_-]+)/(?P<turma_slug>[\w_-]+)/$',
        views.alunos, name='student'
    ),
    url(
        r'^(?P<school_year_slug>[\w_-]+)/(?P<turma_slug>[\w_-]+)/(?P<slug>[\w_-]+)/$',
        views.aluno, name='each_student'
    ),
]
