from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'turmas/', views.turmas, name='turmas'),
    url(r'^(?P<school_year_id>[0-9]+)/$', views.detail, name='detail'),
]
