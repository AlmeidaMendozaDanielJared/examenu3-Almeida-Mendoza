# tienda/forms.py

# Importamos forms de Django para crear formularios
from django import forms
from .models import Producto, Categoria, Proveedor, Cliente, Venta
  # Importamos nuestros modelos


# ============ FORMULARIO PARA PRODUCTOS ============
class ProductoForm(forms.ModelForm):
    """Formulario para crear y editar productos"""

    # Meta clase define la configuración del formulario
    class Meta:
        model = Producto  # El modelo que usará este formulario
        fields = ['nombre', 'descripcion', 'precio_venta', 'stock', 'categoria', 'activo']  # Campos que aparecerán en el formulario

        # Widgets: personalización de cómo se muestran los campos en HTML
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',  # Clase de Bootstrap para estilos
                'placeholder': 'Ingrese el nombre del producto'  # Texto de ayuda en el campo
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,  # Altura del textarea en filas
                'placeholder': 'Ingrese una descripción del producto'
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',  # Permite decimales de 2 dígitos
                'min': '0',  # Valor mínimo
                'placeholder': '0.00'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': '0'
            }),
            # Select para la categoría (combobox con las opciones de categorías)
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            # Checkbox para el campo activo
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        # Labels: etiquetas personalizadas para cada campo
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio_venta': 'Precio ($)',
            'stock': 'Cantidad en Stock',
            'categoria': 'Categoría',
            'activo': '¿Producto Activo?',
        }


# ============ FORMULARIO PARA CATEGORÍAS ============
class CategoriaForm(forms.ModelForm):
    """Formulario para crear y editar categorías"""

    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']  # Solo nombre y descripción

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la categoría'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ingrese una descripción (opcional)'
            }),
        }

        labels = {
            'nombre': 'Nombre de la Categoría',
            'descripcion': 'Descripción',
        }


# ============ FORMULARIO PARA PROVEEDORES ============
class ProveedorForm(forms.ModelForm):
    """Formulario para crear y editar proveedores"""

    class Meta:
        model = Proveedor
        fields = ['nombre', 'empresa', 'telefono', 'email', 'direccion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del contacto'
            }),
            'empresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la empresa'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono de contacto'
            }),
            'email': forms.EmailInput(attrs={  # EmailInput valida formato de email
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Dirección completa'
            }),
        }

        labels = {
            'nombre': 'Nombre del Contacto',
            'empresa': 'Empresa',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'direccion': 'Dirección',
        }


# ============ FORMULARIO PARA CLIENTES ============
class ClienteForm(forms.ModelForm):
    """Formulario para crear y editar clientes"""

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del cliente'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido del cliente'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono de contacto'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Dirección de entrega'
            }),
        }

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
        }


# Formulario de Venta (Simplificado)
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'total']  # Define los campos esenciales para registrar una venta.
