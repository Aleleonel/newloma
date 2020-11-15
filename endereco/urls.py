from django.urls import path
from . import views as v

app_name = 'endereco'

urlpatterns = [
    path('lista/', v.lista_search, name='enderecos_lista'),
    path('add/', v.EnderecoCreate.as_view(), name='endereco_add'),
    path('<int:pk>/', v.endereco_detail, name='enderecos_detail'),
    path('<int:pk>/edit/', v.EnderecoUpdate.as_view(), name='enderecos_edit'),
    path('deletar/<int:pk>/', v.endereco_delete, name='enderecos_delete'),
]