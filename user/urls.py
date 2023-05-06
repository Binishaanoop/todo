from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name='user'),
    path('createAccount', views.user_signup, name='signup'),
    path('login', views.user_login, name='login'),
]