from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from oferta.models import *
from ciudad.models import *

from django.shortcuts import get_object_or_404

# Create your views here.
def cambiar(request, ciudad):
    # return HttpResponse("Ayuda % s" % ciudad) 
    request.session["ciudad_actual"] = ciudad
    return HttpResponseRedirect('/')

def recientes(request, ciudadx):
    ciudades = Ciudad.objects.all()

    try:
        ciudad = Ciudad.objects.get(slug=ciudadx,)
        cercanas = Ciudad.objects.exclude(id=ciudad.id, )[0:5]
        ofertas = Oferta.objects.filter(ciudad_id=ciudad.id, revisada=1, ).order_by("fecha_publicacion")
        relacionadas = Oferta.objects.exclude(ciudad_id=ciudad.id, )
    except ObjectDoesNotExist:
        return HttpResponse("objeto no existe")

    return render(request, 'ciudad/recientes.html', {'ciudadactual' : ciudad,'ciudad' : ciudad, 'cercanas': cercanas, 'ofertas': ofertas, 'ciudades': ciudades})