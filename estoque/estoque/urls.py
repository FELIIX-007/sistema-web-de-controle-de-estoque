from django.contrib import admin
from django.urls import path, include  # Inclua o `include` para importar as URLs de outros apps
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('produtos/', views.pagina_inicial, name='pagina_inicial'),  # Certifique-se de que você está incluindo as URLs do app 'produtos'
    path('', LoginView.as_view(template_name='estoque/login.html'), name='login'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),

]
