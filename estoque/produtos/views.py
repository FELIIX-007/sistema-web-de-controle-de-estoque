from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProdutoForm

# Create your views here.

@login_required
def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/pagina_inicial.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.sucess(request, "Produto cadastrado com sucesso!")
            return redirect('pagina_inicial')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/cadastrar_produto.html', {'form': form})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.sucess(request, "Produto atualizado com sucesso!")
            return redirect('pagina_inicial')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        messages.sucess(request, "Produto excluído com sucesso!")
        return redirect('pagina_inicial')
    return render(request, 'estoque/excluir_produto.html', {'produto': produto})

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'estoque/detalhe_produto.html', {'produto': produto})

def filtro_produtos(request, id):
    produtos = Produto.objects.filter(id=id)
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})


class CustomLoginView(LoginView):
    template_name = 'estoque/login.html'

@login_required
def filtrar_produtos(request):
    produtos = Produto.objects.all()

    if 'id' in request.GET:
        produto_id = request.GET['id']
        produtos = produtos.filter(id=produto_id)
    
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})