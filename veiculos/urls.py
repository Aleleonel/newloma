from django.urls import path
from . import views as v

app_name = 'veiculos'

urlpatterns = [
    path('lista/', v.lista_search, name='veiculos_lista'),
    path('add/', v.VeiculosCreate.as_view(), name='veiculos_add'),
    path('<int:pk>/', v.veiculos_detail, name='veiculos_detail'),
    path('<int:pk>/edit/', v.VeiculosUpdate.as_view(), name='veiculos_edit'),
    path('deletar/<int:pk>/', v.veiculos_delete, name='veiculos_delete'),
]