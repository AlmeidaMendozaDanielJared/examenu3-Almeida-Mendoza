from django.urls import path, include  # Importa la función path para definir rutas.
from . import views  # Importa las vistas de la aplicación actual.
from .views import login_view, logout_view
 # Importa las vistas de autenticación basadas en clases.

urlpatterns = [  # Lista de patrones de URL.
    # Autenticación
    path('login/', login_view, name='login'),  # URL para iniciar sesión.
    path('logout/', logout_view, name='logout'),  # URL para cerrar sesión.
    
    # Dashboard
    path('dashboard/', views.home, name='dashboard'),  # URL para el panel de control.
    
    # CRUD Productos
    path('productos/', views.producto_lista, name='producto_lista'),  # URL para listar productos.
    path('productos/crear/', views.producto_crear, name='producto_crear'),  # URL para crear un producto.
    path('productos/editar/<int:pk>/', views.producto_editar, name='producto_editar'),  # URL para editar un producto específico (usando su PK).
    path('productos/eliminar/<int:pk>/', views.producto_eliminar, name='producto_eliminar'),  # URL para eliminar (desactivar) un producto específico.

    # ============ RUTAS PARA CATEGORÍAS ============
    path('categorias/', views.categoria_lista, name='categoria_lista'),  # Lista todas las categorías
    path('categorias/crear/', views.categoria_crear, name='categoria_crear'),  # Crear categoría
    path('categorias/editar/<int:pk>/', views.categoria_editar, name='categoria_editar'),  # Editar categoría
    path('categorias/eliminar/<int:pk>/', views.categoria_eliminar, name='categoria_eliminar'),  # Eliminar categoría
    
    # ============ RUTAS PARA PROVEEDORES ============
    path('proveedores/', views.proveedor_lista, name='proveedor_lista'),  # Lista todos los proveedores
    path('proveedores/crear/', views.proveedor_crear, name='proveedor_crear'),  # Crear proveedor
    path('proveedores/editar/<int:pk>/', views.proveedor_editar, name='proveedor_editar'),  # Editar proveedor
    path('proveedores/eliminar/<int:pk>/', views.proveedor_eliminar, name='proveedor_eliminar'),  # Eliminar proveedor
    
    # ============ RUTAS PARA CLIENTES ============
    path('clientes/', views.cliente_lista, name='cliente_lista'),  # Lista todos los clientes
    path('clientes/crear/', views.cliente_crear, name='cliente_crear'),  # Crear cliente
    path('clientes/editar/<int:pk>/', views.cliente_editar, name='cliente_editar'),  # Editar cliente
    path('clientes/eliminar/<int:pk>/', views.cliente_eliminar, name='cliente_eliminar'),  # Eliminar cliente

    # La URL raíz redirecciona al dashboard si está autenticado, o a login si no.
    path('', views.home, name='home'),  # URL raíz de la aplicación 'tienda'.
]

# Nota: captura un número entero de la URL y lo pasa como parámetro 'pk' a la vista.
# Por ejemplo: productos/editar/5/ llamará a producto_editar(request, pk=5)
