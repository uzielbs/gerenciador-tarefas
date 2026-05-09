from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('concluir/<int:id>/', views.concluir, name='concluir'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registro/', views.registro, name='registro'),
]
