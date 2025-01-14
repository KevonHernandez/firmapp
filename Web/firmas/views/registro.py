# firmas/views/registro.py
import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Usuario
from firmas.criptografia import convertir_llave_privada_bytes, convertir_llave_publica_bytes, generar_llave_privada, generar_llave_publica, cifrar_llave_privada
from firmas.hasheo import generar_salt, hashear_password, convertir_binario_texto64

def registro(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_completo = request.POST['nombre_completo']
        nick = request.POST['nick']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        correo = request.POST['email']

        # Verificar si las contraseñas coinciden
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('firmas:registro')

        # Generar salt y hashear la contraseña
        salt = generar_salt()
        hash_password, salt = hashear_password(password, salt)

        # Generar y cifrar las llaves
        llave_privada = generar_llave_privada()
        llave_publica = generar_llave_publica(llave_privada)
        llave_privada_pem = convertir_llave_privada_bytes(llave_privada)
        llave_publica_pem = convertir_llave_publica_bytes(llave_publica)
        llave_privada_cifrada, iv, salt_cifrado = cifrar_llave_privada(llave_privada_pem, password)

               # Decodificar el IV antes de pasarlo a convertir_binario_texto64 si es necesario
        if isinstance(iv, str):  # Si el IV está en Base64
            iv = base64.b64decode(iv)
       # Crear el usuario en la base de datos
        nuevo_usuario = Usuario(
            nombre_completo=nombre_completo,
            nick=nick,
            password=hash_password,
            email=correo,
            salt=convertir_binario_texto64(salt),  # salt debe estar en bytes, convertido a base64
            private_key=convertir_binario_texto64(llave_privada_cifrada),  # clave privada cifrada
            public_key=llave_publica_pem.decode('utf-8'),  # clave pública
            iv=convertir_binario_texto64(iv),  # iv debe estar en bytes, convertido a base64
            salt_llave=salt_cifrado  # salt para la llave, convertido a base64
        )

        # Guardar el usuario
        nuevo_usuario.save()

        # Mostrar mensaje de éxito
        messages.success(request, 'Usuario registrado exitosamente.')
        return redirect('firmas:login')

    return render(request, 'firmas/registro.html')