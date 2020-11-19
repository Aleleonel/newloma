from django.urls import path
from . import views as v

app_name = 'account'

urlpatterns = [
    path('', v.registrar, name='registrar'),

]