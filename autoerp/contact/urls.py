from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^(?P<page>[0-9]+)/$', views.index, name='index'),
            url(r'^(?P<page>[0-9]+)/(?P<itemsByPage>[0-9]+)/$', views.index, name='index'),
            url(r'^people/$', views.people_index, name='people_index'),
            url(r'^company/$', views.company_index, name='company_index'),
            url(r'^company/(?P<item_id>[0-9]+)/$', views.company_view, name='company_view'),
                ]
