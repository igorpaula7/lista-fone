from django.urls import path
from contatos.views import ContatoFormView, ContatoListView

urlpatterns = [
    path("criar_contato", ContatoFormView.as_view(), name="criar_contato"),
    path("lista_contato", ContatoListView.as_view(), name="lista_contato"),
]
