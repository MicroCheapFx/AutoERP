from django.conf.urls import url

from . import views

urlpatterns = [
            # ex: /polls/
            url(r'^$', views.index, name='index'),
            url(r'^login/$', views.user_login, name='login'),
            url(r'^logout/$', views.user_logout, name='logout'),
            #url(r'^accounts/login/', views.index, name='login'),
            # ex: /polls/5/
            #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
            # ex: /polls/5/results/
            #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
            # ex: /polls/5/vote/
            #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
                ]
