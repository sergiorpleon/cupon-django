from django import template
register = template.Library()

import re
from datetime import date

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from oferta.models import *
from ciudad.models import *
from tienda.models import *

@register.filter(name='restar')
def restar(valor, arg):
    return valor - arg

@register.filter(name='multiplicar')
def multiplicar(valor, arg):
    return valor * arg

@register.filter(name='faltan')
def faltan(valor):
    now = date.today()
    resta = valor - now
    #a = re.split(',', resta)
    return resta

@register.filter(name='listar')
def listar(valor, arg='ul'):
    html='<%s>\n<li>%s</li>\n</%s>\n' % (arg, valor.replace('\n', '</li>\n</li>'), arg)
    return html

@register.filter(name='expiracion')
def expiracion(valor):
    now = date.today()
    #birthday = date(int('1964'),int('7'),int('31'))
    a = re.split(' ', valor)
    fecha = date(int(a[0]),int(a[1]),int(a[2]))
    age = fecha - now
    return int(re.split(' ', '%s' % age)[0])

@register.filter(name='es_propietario')
def es_propietario(valor):
    try:
        user = User.objects.get(username = valor )
        tienda = Tienda.objects.get(propietario= user.id)
    except ObjectDoesNotExist:
        return 0
    return 1