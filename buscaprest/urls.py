from django.urls import path
from . import views as v

app_name = 'buscaprest'

urlpatterns = [
    path('lista/', v.lista_search, name='buscaprest_lista'),
    path('add/', v.PrestadorCreate.as_view(), name='prestadores_add'),
    path('<int:pk>/', v.prestadores_detail, name='prestadores_detail'),
    path('<int:pk>/edit/', v.PrestadorUpdate.as_view(), name='prestadores_edit'),
    path('deletar/<int:pk>/', v.prestadores_delete, name='prestadores_delete'),
]