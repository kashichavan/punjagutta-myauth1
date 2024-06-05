from django.urls import path
from .views import register

app_name='app1'

urlpatterns = [
    path('register/',register,name='register')

]
