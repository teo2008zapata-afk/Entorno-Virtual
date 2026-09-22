from django.shortcuts import render
from .models import contacto

def crear(request):
    if request.method == 'POST':
        contacto = contacto(
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')
    )
        contacto.save()
        return render(request, 'contactos/formulario.html')
