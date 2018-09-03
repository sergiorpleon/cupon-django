from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.db import models
from oferta.models import *
from ciudad.models import *
from tienda.models import *

from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

from oferta.forms import FormularioOferta
from tienda.forms import FormularioTienda

from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def login_redirect(request):
    return HttpResponseRedirect("/usuario/compras")

def tienda_portada(request, ciudadx, tiendax):
    #return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    request.session["ciudad_actual"] = ciudadx

    try:
        ciudad = Ciudad.objects.get(slug=ciudadx,)
        cercanas = Ciudad.objects.exclude(id=ciudad.id)[0:5]
        tienda = Tienda.objects.get(ciudad_id=ciudad.id, slug=tiendax, )
        ofertas = Oferta.objects.filter(tienda_id=tienda.id, )
        cercanas = Tienda.objects.exclude(id=tienda.id)[0:5]
    except ObjectDoesNotExist:
        return HttpResponse("objeto no existe")

    return render(request, 'tienda/portada.html', {'ciudadactual' : ciudad, 'tienda' : tienda, 'cercanas': cercanas, 'ofertas': ofertas, 'ciudades': ciudades})

def es_propietario(user):
    try:
        user = User.objects.get(username = user.username )
        tienda = Tienda.objects.get(propietario= user.id)
    except ObjectDoesNotExist:
        return 0
    return 1

@user_passes_test(es_propietario, login_url="usuario/login/")
def extranet_portada(request):
    #return HttpResponse( request.user.has_perm('oferta.add_oferta') )  
    ciudades = Ciudad.objects.all()

    try:
        user = User.objects.get(username = request.user.username )
        tienda = Tienda.objects.get(propietario= user.id)
        ofertas = Oferta.objects.filter(tienda_id=tienda.id, )
    except ObjectDoesNotExist:
        return HttpResponse("objeto no existe")

    return render(request, 'extranet/portada.html', {'ofertas': ofertas, 'ciudades': ciudades,}) 

@user_passes_test(es_propietario, login_url="usuario/login/")
def extranet_venta(request, id):
    # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    try:
        user = User.objects.get(username = request.user.username )
        tienda = Tienda.objects.get(propietario= user.id)
        oferta = Oferta.objects.get( id = id, tienda_id=tienda.id)
        ventas = Venta.objects.filter(oferta_id = id, )
    except ObjectDoesNotExist:
        return HttpResponse("objeto no existe")

    return render(request, 'extranet/ventas.html', {'oferta': oferta, 'ventas': ventas, 'ciudades': ciudades,})

@user_passes_test(es_propietario, login_url="usuario/login/")
def extranet_oferta_nueva(request):
    if request.method == 'POST':
        form = FormularioOferta(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            
            try:
                user = User.objects.get(username = request.user.username )
                tienda = Tienda.objects.get(propietario= user.id)
                ciudad = Ciudad.objects.get(id = tienda.ciudad_id)
            except ObjectDoesNotExist:
                return HttpResponse("objeto no existe")

            p = form.save(commit=False)
            p.ciudad = ciudad
            p.tienda = tienda
            p.save()

            return HttpResponseRedirect('/extranet/')
    else:
        form = FormularioOferta()
    return render(request, 'extranet/nueva_oferta.html', {'form': form})

@user_passes_test(es_propietario, login_url="usuario/login/")
def extranet_oferta_editar(request, id):
    if request.method == 'POST':
        form = FormularioOferta(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            try:
                user = User.objects.get(username = request.user.username )
                tienda = Tienda.objects.get(propietario= user.id)
                ciudad = Ciudad.objects.get(id = tienda.ciudad_id)
            except ObjectDoesNotExist:
                return HttpResponse("objeto no existe")
            
            oferta = Oferta.objects.get(id = id)
            p = form.save(commit=False)
            p.id = id
            p.ciudad = ciudad
            p.tienda = tienda
            p.save()


            return HttpResponseRedirect('/extranet/')
    else:
        try:
            oferta = Oferta.objects.get(id = id)
        except ObjectDoesNotExist:
            return HttpResponse("objeto no existe")
        form = FormularioOferta(initial={
            'nombre' :  oferta.nombre,
                'slug' :  oferta.slug,
                'descripcion' :  oferta.descripcion,
                'condiciones' :  oferta.condiciones,
                'photo' :  oferta.photo,
                'precio' :  oferta.precio,
                'descuento' :  oferta.descuento,
                'fecha_expiracion' : oferta.fecha_expiracion,
                #'fecha_publicacion' :  oferta.fecha_publicacion,
                'compra' :  oferta.compra,
                'umbral' :  oferta.umbral,
                'revisada' :  oferta.revisada,
        })
        return render(request, 'extranet/editar_oferta.html', {'form': form, 'id': id})

@user_passes_test(es_propietario, login_url="usuario/login/")
def extranet_perfil(request):
    if request.method == 'POST':
        form = FormularioOferta(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            try:
                user = User.objects.get(username = request.user.username )
                tienda = Tienda.objects.get(propietario= user.id)
                
            except ObjectDoesNotExist:
                return HttpResponse("objeto no existe")

            tienda.nombre = cd['nombre'],
            tienda.slug = cd['slug'],
            tienda.descripcion = cd['descripcion'],
            tienda.direccion = cd['direccion'],
                
            tienda.save()

            return HttpResponseRedirect('/extranet/')
    else:
        try:
            user = User.objects.get(username = request.user.username )
            tienda = Tienda.objects.get(propietario= user.id)
        except ObjectDoesNotExist:
            return HttpResponse("objeto no existe")

        form = FormularioTienda(initial={
            'nombre' :  tienda.nombre,
                'slug' :  tienda.slug,
                'descripcion' :  tienda.descripcion,
                'direccion' :  tienda.direccion,
        })
        return render(request, 'extranet/perfil.html', {'form': form, 'id': tienda.id})
 
    
