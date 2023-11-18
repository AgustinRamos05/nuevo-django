from django.urls import path
from iphone.views import ListadoProductos, CrearIphone, ActualizarIphone, DetalleIphone, EliminarIphone

urlpatterns = [
    path('iphone/',ListadoProductos.as_view(), name= 'iphone'),
    path('iphone/crear', CrearIphone.as_view(), name='crear_iphone' ),
    path('iphone/<int:pk>', DetalleIphone.as_view(), name='detalle_producto' ),
    path('iphone/<int:pk>/actualizar', ActualizarIphone.as_view(), name='actualizar_producto' ),
    path('iphone/<int:pk>/eliminar',EliminarIphone.as_view() , name='eliminar_producto')
]
