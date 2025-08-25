from django.urls import path
from contatos.views import ContatoFormView

urlpatterns = [
    path("criar_contato", ContatoFormView.as_view(), name="criar_contato"),
]