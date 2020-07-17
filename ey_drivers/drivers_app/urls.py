from django.urls import path

from . import views

app_name = 'drivers_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:driver_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:driver_id>/vote/', views.vote, name='vote'),
]