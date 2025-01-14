import base64
#from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from firmas.criptografia import descifrar_llave_privada
from firmas.decorators import sesion_requerida
from firmas.firmar import  firmar_archivo2
from firmas.hasheo import password_valido
from ..models import Usuario
#from django.core.files.storage import FileSystemStorage

def safe_base64_decode(data):
    """Decodifica un string base64 asegurando que tenga el relleno adecuado."""
    try:
        print(f"Datos originales: {data}")
        padding_needed = 4 - len(data) % 4
        if padding_needed:
            data += '=' * padding_needed
        decoded_data = base64.b64decode(data)
        
        return decoded_data
    except Exception as e:
       
        raise
    
@sesion_requerida
def home(request):
    # logica para el boton cerrar sesion
    if request.method == 'POST' and request.POST.get('cerrar_sesion') == 'true':
        if 'ha_iniciado_sesion' in request.session:
            del request.session['ha_iniciado_sesion']
        if 'nick' in request.session:
            del request.session['nick']
        return redirect('firmas:login')
    
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        password = request.POST.get('password')

        if not archivo:
            messages.error(request, "No se seleccionó un archivo para firmar.")
            return render(request, 'firmas/home.html')

        if not password:
            messages.error(request, "Por favor, introduce tu contraseña.")
            return render(request, 'firmas/home.html')

        try:
            nick = request.session.get('nick')
            
            usuario = get_object_or_404(Usuario, nick=nick)

            if not usuario.private_key:
                messages.error(request, "El usuario no tiene una clave privada registrada.")
                return render(request, 'firmas/home.html')

                       
            salt = base64.b64decode(usuario.salt)
            iv = usuario.iv

            if not password_valido(password, usuario.password, salt):
                messages.error(request, "La contraseña es incorrecta.")
                return render(request, 'firmas/home.html')

            print("Verificando la contraseña e intentando descifrar la clave privada.")
            llave_privada = descifrar_llave_privada(usuario.private_key, password, iv, usuario.salt_llave)
          
        except Exception as e:
            messages.error(request, f"Error al firmar el archivo")
            return render(request, 'firmas/home.html')

        # Proceso de firma
        try:
            filename=archivo.name
            byts = archivo.read()

            archivo_firmado = firmar_archivo2(byts, llave_privada)
            base64_data = base64.b64encode(archivo_firmado).decode('utf-8')

            response = render(request, 'firmas/descarga.html', {'filename': filename, "file":  base64_data })            
       
            return response

        except Exception as e:
            messages.error(request, f"Error al firmar el archivo")
            return render(request, 'firmas/home.html')

    return render(request, 'firmas/home.html')