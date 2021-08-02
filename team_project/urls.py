from django.contrib import admin
from django.urls import path
from rango import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.user_login, name = 'login'),
    path('rango/', include('rango.urls')),
]
