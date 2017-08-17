from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^todos_anos_letivos/$',
        views.all_school_years_func, name='all_school_years'
        ),
    url(r'^todas_escolas/$',
        views.all_schools_func, name='all_schools'
        ),
    url(r'^(?P<slug>[\w_-]+)/$', views.index, name='index1'),
    url(
        r'^(?P<school_year_slug>[\w_-]+)/(?P<school_class_slug>[\w_-]+)/$',
        views.school_class_func, name='schoolclass'
    ),
    url(r'^(?P<school_year_slug>[\w_-]+)/(?P<school_class_slug>[\w_-]+)/(?P<slug>[\w_-]+)/$',
        views.student_profile_func, name='student'
        ),
]
