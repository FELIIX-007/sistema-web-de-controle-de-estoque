from django import forms
from .models import Produto
from django.contrib.auth.forms import AuthenticationForm
from django.utils.timezone import now

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'data_cadastro']

    data_cadastro = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=now  # Define a data inicial como hoje
    )

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))