from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'drivers_app'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('drivers/', views.drivers_list),
    # path('drivers/<int:pk>/', views.drivers_detail),
    # path('schedule/', views.schedule_list),
    # path('schedule/<int:pk>/', views.schedule_detail),
    path('drivers/', views.DriversList.as_view()),
    path('drivers/<int:pk>/', views.DriversDetail.as_view()),
    path('schedule/', views.ScheduleList.as_view()),
    path('schedule/<int:pk>/', views.ScheduleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
