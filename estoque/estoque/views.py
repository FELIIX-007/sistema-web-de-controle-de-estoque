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

@login_required
def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)

    if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")  # ✅ Mensagem de sucesso
            return redirect("pagina_inicial")  
    else:
            messages.error(request, "Usuário ou senha incorretos.")  # ✅ Mensagem de erro
            return render(request, "login.html")


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

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST.get('nomeProduto')
        produto.descricao = request.POST.get('descricaoProduto')
        produto.quantidade = int(request.POST.get('quantidadeProduto', produto.quantidade))
        # Substitui a vírgula pelo ponto antes de converter
        preco_str = request.POST.get("precoProduto").replace(",", ".")  
        try:
            produto.preco = float(preco_str)  # Converte para float
        except ValueError:
            messages.error(request, "Erro: O preço deve ser um número válido.")
            return render(request, "estoque/editar_produto.html", {"produto": produto})

        produto.save()

        messages.success(request, "Produto atualizado com sucesso!")
        return redirect('pagina_inicial')  # Redirecione para a página desejada

    return render(request, 'estoque/editar_produto.html', {'produto': produto})


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


@login_required
class CustomLoginView(LoginView):
    template_name = 'estoque/login.html'
