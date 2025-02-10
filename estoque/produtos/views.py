from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Produto
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/pagina_inicial.html')

class CustomLoginView(LoginView):
    template_name = 'estoque/login.html'

@login_required
def filtrar_produtos(request):
    produtos = Produto.objects.all()

    if 'id' in request.GET:
        produto_id = request.GET['id']
        produtos = produtos.filter(id=produto_id)
    
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})