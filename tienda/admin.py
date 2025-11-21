from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Cliente, PerfilUsuario

# ============ CONFIGURACIÓN DEL ADMIN PARA PERFILES DE USUARIO ============
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol', 'departamento', 'activo', 'fecha_contratacion')
    list_filter = ('rol', 'activo', 'departamento')
    search_fields = ('user__username', 'user__email', 'departamento')
    list_editable = ('rol', 'activo')
    ordering = ('-fecha_contratacion',)

# ============ CONFIGURACIÓN DEL ADMIN PARA CATEGORÍAS ============
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion',)
    ordering = ('nombre',)

# ============ CONFIGURACIÓN DEL ADMIN PARA PRODUCTOS ============
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio_venta', 'stock', 'activo', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria', 'activo', 'fecha_creacion')
    list_editable = ('precio_venta', 'stock', 'activo')
    ordering = ('-fecha_creacion',)

# ============ CONFIGURACIÓN DEL ADMIN PARA PROVEEDORES ============
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    # Quitamos fecha_registro porque no existe en el modelo
    list_display = ('id', 'nombre', 'empresa', 'telefono', 'email')
    search_fields = ('nombre', 'empresa', 'email')
    list_filter = ()  # No hay campos para filtrar
    ordering = ('empresa',)

# ============ CONFIGURACIÓN DEL ADMIN PARA CLIENTES ============
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('fecha_registro',)
    ordering = ('apellido', 'nombre')
