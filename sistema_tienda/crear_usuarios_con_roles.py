import django
import os

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_tienda.settings')
django.setup()

from django.contrib.auth.models import User
from tienda.models import PerfilUsuario

usuarios = [
    {'username': 'vendedor1', 'password': 'vendedor123', 'rol': 'vendedor', 'departamento': 'Ventas', 'telefono': '555-1111'},
    {'username': 'gerente1', 'password': 'gerente123', 'rol': 'gerente', 'departamento': 'Gerencia', 'telefono': '555-2222'},
    {'username': 'admin1', 'password': 'admin123', 'rol': 'administrador', 'departamento': 'Sistemas', 'telefono': '555-3333'},
]

for data in usuarios:
    user, created = User.objects.get_or_create(username=data['username'])
    if created:
        user.set_password(data['password'])
        user.save()
        PerfilUsuario.objects.create(
            user=user,
            rol=data['rol'],
            departamento=data['departamento'],
            telefono=data['telefono']
        )
        print(f"✅ Usuario {data['username']} creado con rol {data['rol']}")
    else:
        print(f"⚠️ Usuario {data['username']} ya existe")
