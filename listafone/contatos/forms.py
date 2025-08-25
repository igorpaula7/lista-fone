from django.forms import ModelForm
from contatos.models import Categoria, Contato


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = [
            "nome", 
            "telefone", 
            "email", 
            "favorito",
            "emergencia",
        ]