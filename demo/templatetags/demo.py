from django import template

register = template.Library()
@register.filter
def pendiente(coevaluacion, user):
    contestadas, integrantes = coevaluacion.pendiente(user)
    print(contestadas)
    print(integrantes)
    return contestadas < integrantes - 1