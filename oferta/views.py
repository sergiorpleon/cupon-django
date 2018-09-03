from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from oferta.models import *
from ciudad.models import *

from django.shortcuts import get_object_or_404

def oferta(request, ciudad, slug):
    # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    try:
        ciudad = Ciudad.objects.get(slug=ciudad, )
        oferta = Oferta.objects.get(ciudad_id=ciudad.id, slug=slug)
        relacionadas = Oferta.objects.exclude(ciudad_id=ciudad.id, )
    except ObjectDoesNotExist:
        return HttpResponse("objeto no existe")

    return render(request, 'oferta/detalle.html', {'oferta': oferta, 'ciudades': ciudades, 'relacionadas' : relacionadas}) 