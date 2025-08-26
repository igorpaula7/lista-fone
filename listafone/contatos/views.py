from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.db import transaction
from contatos.forms import ContatoForm
from contatos.models import Contato
from django.views.generic.list import ListView


class ContatoFormView(FormView):
    template_name = "base_form.html"
    form_class = ContatoForm
    success_url = reverse_lazy("criar_contato")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cadastrar Contato"
        return context

    # Esse decorator garante que a transação seja feita de forma atomica
    # ou seja, se der errado, ele desfaz tudo
    @transaction.atomic
    def form_valid(self, form):
        # o try é obrigatorio para o decorator
        try:
            contato = form.save(commit=False)
            contato.save()
            messages.success(self.request, "Contato salvo com sucesso!")
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Erro ao salvar o contato: {str(e)}")
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrija os erros abaixo.")
        return super().form_invalid(form)

    # success_url = "/criar_contato/"


class ContatoListView(ListView):
    template_name = "lista.html"
    model = Contato
    context_object_name = "dados"
