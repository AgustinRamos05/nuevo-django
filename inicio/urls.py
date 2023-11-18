from django.urls import path
from inicio.views import inicio, iphones, comprar_iphone, eliminar, actualizar, detalle_iphone

urlpatterns = [
    path('', inicio, name='inicio'),
    path('iphone/', iphones, name='productos'),
    path('inicio/comprar/', comprar_iphone, name='comprar_iphone'),
    path('inicio/<int:iphone_id>/eliminar', eliminar, name='eliminar'),
    path('inicio/<int:iphone_id>/actualizar', actualizar, name='actualizar'),
    path('inicio/<int:iphone_id>/detalle_iphone', detalle_iphone, name='detalle_iphone')
]
