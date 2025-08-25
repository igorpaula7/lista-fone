from django.shortcuts import render, redirect
from contatos.forms import ContatoForm
from django.views.generic.edit import FormView


class ContatoFormView(FormView):
    template_name = "criar_contato.html"
    form_class = ContatoForm
    success_url = "/criar_contato/"