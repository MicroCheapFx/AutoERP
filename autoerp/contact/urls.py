from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^$', views.index, name='index'),
            url(r'^personne', views.personne_index, name='personne_index'),
            url(r'^entreprise', views.entreprise_index, name='entreprise_index'),
                ]
