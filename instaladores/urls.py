from django.urls import path
from . import views as v
app_name = 'instaladores'

urlpatterns = [
    path('lista', v.instaladores_list, name='instaladores_list' ),

    path('add/', v.InstaladoresCreate.as_view(), name='instaladores_add'),
    path('<int:pk>/', v.instaladores_detail, name='instaladores_detail'),
    path('<int:pk>/edit/', v.InstaladoresUpdate.as_view(), name='instaladores_edit'),
    path('deletar/<int:pk>/', v.instaladores_delete, name='instaladores_delete'),
]
