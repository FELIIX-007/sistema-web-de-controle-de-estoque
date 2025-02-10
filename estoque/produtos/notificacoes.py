from .models import Produto
from django.core.mail import send_mail

def verificar_estoque_baixo():
    produtos_baixo_estoque = Produto.objects.filter(quantidade__lt=5)  
    for produto in produtos_baixo_estoque:
        send_mail(
            'Alerta de estoque baixo',
            f'O produto {produto.nome} está com estoque baixo.',
            'from@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )
