"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from funzioni_iot import views  as views_app_iot
from funzioni_iot.views import titoloDetailView, TitoloDetailViewCB, home
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static




sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hellocontattaci', views_app_iot.hellocontattaci),
    path('creatitoli', views_app_iot.crea_titoli),
    path('visuatitoli', views_app_iot.visuatitoli),
    path('homeiot', views_app_iot.homeiot),
    path('homeTitoly', views_app_iot.homeTitoly),
    path('modificatitolo', views_app_iot.mod_titoli),
    path('cancellatitolo', views_app_iot.can_titoli),
    path('prova_django', views_app_iot.prova_django),
    path('blog/', include('blog.urls', namespace='blog')),
    path('titoli2/', include('funzioni_iot.urls', namespace='titol')),
    path('titoli2/titolosingolo/<int:pk>', titoloDetailView, name ='titolo_detail'),
    path('about2/', include('funzioni_iot.urls', namespace='titol')),
    path('risposta_endpoint', views_app_iot.risposta_rest),
    path('clienti', include('funzioni_iot.urls')),
    path('mail', views_app_iot.invio_mail),
    #
    # url  di tipo REST
    path('chiamata_request', views_app_iot.chiamata_request),
    path('chiamata_request_payload', views_app_iot.chiamata_request_payload),
    path('risposta_endpoint', views_app_iot.risposta_rest),
    path('risposta_collection', views_app_iot.cliente_collection),

 

    
]


urlpatterns += [
    path('', views_app_iot.homep),
    path('registrazione/', views_app_iot.registrazione),
    path('base/', views_app_iot.base),
    path('accounts/loginenrico/', views_app_iot.login),
    path('accounts/logoutenrico/', views_app_iot.logout_enrico),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('shopp', include('shop.urls', namespace='shop')),
    path('cart', include('cart.urls', namespace='cart')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)