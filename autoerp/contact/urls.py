from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^people/$', views.people_index, name='people_index'),
            url(r'^company/$', views.company_index, name='company_index'),
                ]
