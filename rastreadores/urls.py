from django.urls import path
from . import views as v

app_name = 'rastreadores'

urlpatterns = [
    path('lista/', v.lista_search, name='rastreadores_lista'),
    path('add/', v.RastreadoresCreate.as_view(), name='rastreadores_add'),
    path('<int:pk>/', v.rastreadores_detail, name='rastreadores_detail'),
    path('<int:pk>/edit/', v.RastreadoresUpdate.as_view(), name='rastreadores_edit'),
    path('deletar/<int:pk>/', v.rastreadores_delete, name='rastreadores_delete'),
]