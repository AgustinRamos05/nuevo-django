from django.urls import path
from inicio.views import inicio, iphones, comprar_iphone

urlpatterns = [
    path('', inicio, name='inicio'),
    path('iphone/', iphones, name='productos'),
    path('inicio/comprar/', comprar_iphone, name='comprar_iphone')
]
