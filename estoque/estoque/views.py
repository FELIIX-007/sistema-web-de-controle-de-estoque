from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pagina_inicial')  # Redireciona para a página inicial após login
    else:
        form = AuthenticationForm()
    
    return render(request, 'produtos/login.html', {'form': form})


@login_required
def pagina_inicial(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/pagina_inicial.html', {'produtos': produtos})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nomeProduto')
        descricao = request.POST.get('descricaoProduto')
        quantidade = request.POST.get('quantidadeProduto')
        preco = request.POST.get('precoProduto')
        data_cadastro = timezone.now().date()  # Apenas a data, sem a parte da hora

        produto = Produto(
            nome=nome,
            descricao=descricao,
            quantidade=quantidade,
            preco=preco,
            data_cadastro=data_cadastro
        )
        produto.save()

        messages.success(request, "Produto cadastrado com sucesso!")
        return redirect('pagina_inicial')

    # Passar a data atual para o template, também no formato YYYY-MM-DD
    data_atual = '2025-02-12'  # Apenas a data (sem o horário)
    return render(request, 'estoque/cadastrar_produto.html', {'data_atual': data_atual})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nomeProduto')
        produto.descricao = request.POST.get('descricaoProduto')
        produto.quantidade = request.POST.get('quantidadeProduto')
        produto.preco = request.POST.get('precoProduto')
        produto.data_cadastro = request.POST.get('dataCadastro')  # Caso necessário
        produto.save()

        messages.success(request, "Produto atualizado com sucesso!")
        return redirect('pagina_inicial')  # Redirecione para a página desejada

    return render(request, 'estoque/editar_produto.html', {'produto': produto}, produto_id=produto.id)

@login_required
def excluir_produto(request, produto_id):
    if request.method == 'POST':  # Verifique se é uma requisição POST
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect('pagina_inicial')  # Redireciona após a exclusão
    return redirect('pagina_inicial')  # Se não for POST, apenas redireciona

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'estoque/detalhe_produto.html', {'produto': produto})

@login_required
def filtro_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos cadastrados
    return render(request, 'estoque/listar_produtos.html', {'produtos': produtos})



class CustomLoginView(LoginView):
    template_name = 'estoque/login.html'
