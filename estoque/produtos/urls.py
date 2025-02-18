from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views
from .views import editar_produto

urlpatterns = [
    path('login/', LoginView.as_view(template_name='estoque/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Produtos
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('editar/<int:id>/', editar_produto, name='editar_produto'),
    
]
