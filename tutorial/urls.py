from django.conf.urls import url, include
from snippets import views
from django.contrib import admin
from django.conf import settings
from rest_framework.routers import DefaultRouter
# from django.conf.urls.defaults import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
router.register(r'marcas', views.MarcaViewSet)
router.register(r'tipos', views.TipoViewSet)
router.register(r'equipos', views.EquipoViewSet)



# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	url(r'^buscar/(?P<pk>[0-9a-z]+)/$', views.hello, name='pk'),
	url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


