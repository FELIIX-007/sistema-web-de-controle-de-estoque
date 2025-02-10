from .models import Produto, MovimentoEstoque

def registrar_movimento(produto_id, quantidade, tipo_movimento):
    produto = Produto.objects.get(id=produto_id)
    movimento = MovimentoEstoque.objects.create(
        produto=produto,
        quantidade=quantidade,
        tipo_movimento=tipo_movimento
    )
    if tipo_movimento == 'entrada':
        produto.quantidade += quantidade
    elif tipo_movimento == 'saida':
        produto.quantidade -= quantidade
    produto.save()
    movimento.save()
    return movimento
