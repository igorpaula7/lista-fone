import datetime
from django import template

register = template.Library()


@register.filter
def attr(obj, name):
    return getattr(obj, name, "")


@register.filter
def fields(obj):
    if hasattr(obj, '_meta'):
        return obj._meta.fields
    return []

@register.filter
def getattr_filter(obj, attr_name):
    """
    Filtro para acessar atributos de um objeto no template
    Uso: {{ objeto|getattr:"nome_do_atributo" }}
    """
    if hasattr(obj, attr_name):
        value = getattr(obj, attr_name)
        # Formatação de campos específicos
        if value is None:
            return "-"
        elif isinstance(value, bool):
            return "Sim" if value else "Não"
        elif hasattr(value, 'strftime'):  # Para campos de data/hora
            return value.strftime('%d/%m/%Y %H:%M')
        return value
    return "-"
