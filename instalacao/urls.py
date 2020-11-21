from django.urls import path
from . import views as v
app_name = 'instalacao'

urlpatterns = [
    path('lista', v.instalacao_list, name='instalacao_list' ),

    path('add/', v.InstalacaoCreate.as_view(), name='instalacao_add'),
    path('<int:pk>/', v.instalacao_detail, name='instalacao_detail'),
    path('<int:pk>/edit/', v.InstalacaoUpdate.as_view(), name='instalacao_edit'),
    path('deletar/<int:pk>/', v.instalacao_delete, name='instalacao_delete'),
]
