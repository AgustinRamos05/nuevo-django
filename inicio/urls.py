from django.urls import path
from inicio.views import inicio, iphones

urlpatterns = [
    path('', inicio, name='inicio'),
    path('iphone/', iphones, name='productos')
]
