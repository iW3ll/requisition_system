from django.urls import path
from .views import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('cadastrar-estudante/', views.cadastrar_estudante, name='cadastrar_estudante'),
    path('requisicoes/', views.listar_requisicoes, name='listar_requisicoes'),
]
