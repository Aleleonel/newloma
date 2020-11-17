from django.urls import path
from core import views as v

app_name = 'core'
urlpatterns = [
    path('', v.login_user),
    path('submit', v.login_submit),

]
