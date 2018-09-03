from django.contrib import admin
from oferta.models import Oferta, Venta
from tienda.models import Tienda
from ciudad.models import Ciudad

admin.site.register(Oferta)
admin.site.register(Tienda)
admin.site.register(Ciudad)
admin.site.register(Venta)