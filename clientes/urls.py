from django.urls import path
from . import views as v

app_name = 'clientes'

urlpatterns = [
    path('lista/', v.lista_search, name='clientes_lista'),
    path('add/', v.ClientesCreate.as_view(), name='clientes_add'),
    path('<int:pk>/', v.clientes_detail, name='clientes_detail'),
    path('<int:pk>/edit/', v.ClientesUpdate.as_view(), name='clientes_edit'),
    path('deletar/<int:pk>/', v.clientes_delete, name='clientes_delete'),
]