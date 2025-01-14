# main.py
import os
from tkinter.ttk import _Padding
from criptografia import generar_llave_privada, convertir_llave_privada_bytes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

from firmas import hasheo

def firmar_archivo(ruta_archivo, llave_privada):
    # Leer el archivo
    with open(ruta_archivo, 'rb') as archivo:
        contenido = archivo.read()

    # Firmar el contenido del archivo
    firma = llave_privada.sign(
        contenido,
        _Padding.PSS(
            mgf=_Padding.MGF1(hasheo.SHA256()),
            salt_length=_Padding.PSS.MAX_LENGTH
        ),
        hasheo.SHA256()
    )

    # Crear un nuevo archivo que contenga la firma
    nombre_firmado = f"{ruta_archivo}_firmado"
    with open(nombre_firmado, 'wb') as archivo_firmado:
        archivo_firmado.write(firma)

    return nombre_firmado

# Paso 1: Generar una clave privada
llave_privada = generar_llave_privada()

# (Opcional) Guardar la clave privada en un archivo
llave_privada_pem = convertir_llave_privada_bytes(llave_privada)
with open("llave_privada.pem", "wb") as f:
    f.write(llave_privada_pem)

# Paso 2: Firmar un archivo en el directorio `home`
nombre_archivo = "mi_archivo.txt"  # Cambia esto por el nombre de tu archivo
ruta_archivo = os.path.expanduser(f"~/Documentos/{nombre_archivo}")

# Firmar el archivo
archivo_firmado = firmar_archivo(ruta_archivo, llave_privada)

print(f"Archivo firmado creado: {archivo_firmado}")
