# tienda/models.py
from django.db import models # Importa el módulo base de modelos de Django.
from django.contrib.auth.models import User # Importa el modelo de Usuario predeterminado de Django.

# ============ MODELO PERFIL DE USUARIO ============
class PerfilUsuario(models.Model):
    ROLES = (
        ('vendedor', 'Vendedor'),
        ('gerente', 'Gerente'),
        ('administrador', 'Administrador'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='vendedor')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    fecha_contratacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_rol_display()}"
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
    
        # Métodos para verificar roles
    def es_vendedor(self):
            return self.rol == 'vendedor'
        
    def es_gerente(self):
            return self.rol == 'gerente'
        
    def es_administrador(self):
            return self.rol == 'administrador'
        
    def tiene_permiso_lectura(self):
            # Todos pueden leer
            return True
        
    def tiene_permiso_escritura(self):
            # Gerente y Administrador pueden escribir
            return self.rol in ['gerente', 'administrador']
        
    def tiene_permiso_eliminacion(self):
            # Solo Administrador puede eliminar
            return self.rol == 'administrador'


# ============ MODELO CATEGORÍA ============
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

# Modelo 2: Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=150) # Nombre del proveedor.
    contacto = models.CharField(max_length=100, blank=True) # Nombre del contacto, opcional.
    telefono = models.CharField(max_length=15, blank=True) # Número de teléfono, opcional.
    empresa = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    
    # Te recomiendo arreglar este también, por si acaso:
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre # Representación en string del objeto.

# Modelo 3: Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2) # Campo decimal para el precio (máx. 10 dígitos, 2 decimales).
    stock = models.IntegerField(default=0) # Cantidad en inventario, valor predeterminado 0.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # Relación uno a muchos con Categoria (si se borra la categoría, se borran los productos).
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True) # Relación con Proveedor (opcional, si se borra el proveedor, se establece a NULL).
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='productos_creados') # Usuario que creó el producto (opcional, si se borra el usuario, se establece a NULL).
    fecha_creacion = models.DateTimeField(auto_now_add=True) # Fecha y hora de creación (se establece automáticamente al crear).
    activo = models.BooleanField(default=True) # Campo booleano para eliminación lógica (determina si está activo o desactivado).

    def __str__(self):
        return self.nombre # Representación en string del objeto.

# Modelo 4: Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del cliente
    apellido = models.CharField(max_length=100)  # Apellido del cliente
    email = models.EmailField(max_length=191, unique=True)  # Email único (no puede repetirse) - max 191 para MySQL utf8mb4
    telefono = models.CharField(max_length=15)  # Teléfono del cliente
    direccion = models.TextField()  # Dirección de entrega
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Fecha de registro automática
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Muestra nombre completo
    
    # Propiedad que concatena nombre completo
    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['apellido', 'nombre']  # Ordena por apellido y luego por nombre


# Modelo 5: Venta (Transacción)
class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True) # Fecha y hora de la venta.
    total = models.DecimalField(max_digits=10, decimal_places=2) # Total de la venta.
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True) # Cliente asociado (opcional, SET_NULL al eliminar cliente).
    vendido_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Usuario que realizó la venta (opcional, SET_NULL al eliminar usuario).

    def __str__(self):
         return f"Venta #{self.id} - Total: {self.total}" # Representación en string con ID y total.