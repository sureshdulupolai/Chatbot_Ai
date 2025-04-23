from django.urls import path
from . import views as v

app_name = 'AiBot'

urlpatterns = [
    path('', v.AiHomePageFunction, name='AiHomePage'),
]