from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cupon.views.portada', name='portada'),
    url(r'^(?P<ciudadx>\w+)/recientes$', 'ciudad.views.recientes', name='ciudad_recientes'),
    url(r'^usuario/compras$', 'cupon.views.compras', name='compras'),
    url(r'^comprar/(?P<id>\d+)$', 'cupon.views.comprar', name='comprar'),
         
    url(r'^(?P<ciudad>\w+)/ofertas/(?P<slug>\w+)$', 'oferta.views.oferta', name='oferta'),
    url(r'^(?P<ciudadx>\w+)/tiendas/(?P<tiendax>\w+)$', 'tienda.views.tienda_portada', name='tienda_portada'),
    url(r'^usuario/login$', 'cupon.views.login', name='usuario_login'),
    url(r'^usuario/logout$', 'cupon.views.logout', name='usuario_logout'),
    url(r'^usuario/registrar$', 'cupon.views.registrar', name='usuario_registrar'),
    url(r'^usuario/perfil$', 'cupon.views.perfil', name='usuario_perfil'),
     
    url(r'^ciudad/cambiar-a-(?P<ciudad>\w+)$', 'ciudad.views.cambiar', name='cambiar'),
    
    url(r'^extranet/$', 'tienda.views.extranet_portada', name='extranet_portada'),
    url(r'^extranet/oferta/nueva$', 'tienda.views.extranet_oferta_nueva', name='extranet_oferta_nueva'),
    url(r'^extranet/oferta/editar/(?P<id>\d+)$', 'tienda.views.extranet_oferta_editar', name='extranet_oferta_editar'),
    url(r'^extranet/ventas/(?P<id>\d+)$', 'tienda.views.extranet_venta', name='extranet_venta'),
    url(r'^extranet/perfil$', 'tienda.views.extranet_perfil', name='extranet_perfil'),
    url(r'^extranet/usuario/login/$', 'tienda.views.login_redirect', name='login_redirect'),


    url(r'^contacto/$', 'cupon.views.contacto', name='contacto'),

    # url(r'^blog/', include('blog.urls')),
    url(r'^ayuda/$', 'cupon.views.estatica', {'plantilla': 'estaticas/ayuda.html' }, name='ayuda' ),
    url(r'^nosotros/$', 'cupon.views.estatica', {'plantilla': 'estaticas/nosotros.html' }, name='nosotros' ),
    url(r'^privacidad/$', 'cupon.views.estatica', {'plantilla': 'estaticas/privacidad.html' } , name='privacidad'),
    
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
