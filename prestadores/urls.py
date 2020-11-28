"""prestadores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),

    path('prestadores/', include('buscaprest.urls')),
    path('rastreadores/', include('rastreadores.urls')),

    path('veiculos/', include('veiculos.urls')),
    path('enderecos/', include('endereco.urls')),
    path('clientes/', include('clientes.urls')),
<<<<<<< HEAD

    path('instalacao/', include('instalacao.urls')),
    path('instaladores/', include('instaladores.urls')),

=======
    path('instaladores/', include('instaladores.urls')),
>>>>>>> busca
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),

]