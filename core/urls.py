from django.urls import path
from . import views as v

app_name = 'core'

urlpatterns = [
    path('login/', v.login_user, name='login_user'),
    path('login/submit', v.submit_login, name='submit_login'),
    path('', v.home, name='home'),
]