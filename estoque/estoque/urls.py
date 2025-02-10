from django.contrib import admin
from django.urls import path, include  # Inclua o `include` para importar as URLs de outros apps
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),  # Certifique-se de que você está incluindo as URLs do app 'produtos'
    path('login/', LoginView.as_view(template_name='estoque/login.html'), name='login'),  # URL de login
]
