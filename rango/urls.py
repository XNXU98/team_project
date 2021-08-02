from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
path('', views.user_login, name='login'),
]
