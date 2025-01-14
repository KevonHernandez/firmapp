from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import base64
from firmas.models import Usuario
from firmas.views.funcion_verificar_firma import verificar_firma

def validar_firma(request):
        # logica para el boton cerrar sesion
    if request.method == 'POST' and request.POST.get('cerrar_sesion') == 'true':
        if 'ha_iniciado_sesion' in request.session:
            del request.session['ha_iniciado_sesion']
        if 'nick' in request.session:
            del request.session['nick']
        return redirect('firmas:login')
    
    if request.method == 'POST':

        archivo = request.FILES.get('archivofirmado')
        firma = request.FILES.get('firma')
        nombre_firmante = request.POST.get('nombre_firmante')

        if not archivo or not firma or not nombre_firmante:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect('firmas:home')

        try:
            archivo_bytes = archivo.read()
            firma_bytes = firma.read()
            
            # Cargar la clave pública del firmante (esto puede variar según cómo almacenamos o recuperamos la clave pública)
            usuario = get_object_or_404(Usuario, nick=nombre_firmante)
            llave_publica = load_pem_public_key(usuario.public_key.encode())

            # Verificar la firma
            es_valida = verificar_firma(archivo_bytes, firma_bytes, llave_publica)

            if es_valida:
                messages.success(request, "La firma es válida.")
            else:
                messages.error(request, "La firma no es válida.")
        except Exception as e:
            messages.error(request, f"Error al verificar la firma: {str(e)}")

        return redirect('firmas:home')

    return render(request, 'firmas/home.html')
