from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.vote, name='firstdigi'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('all_digi/', views.all_digi, name='all_digi'),
    path('acq_digi/', views.acq_digi, name='acq_digi'),
    path('my_digi/', views.my_digi, name='my_digi'),
]