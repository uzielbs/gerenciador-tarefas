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
    # API
    path('api/tarefas/', views.TarefaListCreateAPI.as_view(), name='api-tarefas'),
    path('api/tarefas/<int:pk>/', views.TarefaDetailAPI.as_view(), name='api-tarefa-detail'),
]
