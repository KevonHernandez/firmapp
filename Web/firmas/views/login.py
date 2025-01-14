# views/login.py
import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Usuario
from ..hasheo import password_valido

def login(request):
    if request.method == 'POST':
        nick = request.POST.get('nick', '').strip()
        password = request.POST.get('password', '').strip()

        errores = []

        if not nick or not password:
            errores.append('El nombre de usuario y la contraseña no pueden estar vacíos.')

        if errores:
            return render(request, 'firmas/login.html', {'errores': errores})

        try:
            usuario = Usuario.objects.get(nick=nick)
            salt = base64.b64decode(usuario.salt)

            if password_valido(password, usuario.password, salt):
                request.session['nick'] = usuario.nick
                request.session['ha_iniciado_sesion'] = True
                request.user = usuario  # Asegurarse de que request.user es el usuario autenticado

                return redirect('firmas:home')
            else:
                messages.error(request, 'Contraseña o Usuario incorrectos.')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')

    return render(request, 'firmas/login.html')
