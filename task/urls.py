from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.home, name='home'),
    path('addTask', views.add_task, name='add_task'),
    path('viewTask', views.view_task, name='view_task'),
    
]    
   