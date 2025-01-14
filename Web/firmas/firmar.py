import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, ec

# def firmar_archivo(ruta_archivo, llave_privada):
#     # Leer el archivo
#     with open(ruta_archivo, 'rb') as archivo:
#         contenido = archivo.read()

#     # Firmar el contenido del archivo
#     firma = llave_privada.sign(
#         contenido,
#         padding.PSS(
#             mgf=padding.MGF1(hashes.SHA256()),
#             salt_length=padding.PSS.MAX_LENGTH
#         ),
#         hashes.SHA256()
#     )

#     # Crear un nuevo archivo que contenga la firma
#     nombre_firmado = f"{ruta_archivo}_firmado"
#     with open(nombre_firmado, 'wb') as archivo_firmado:
#         archivo_firmado.write(firma)

#     return nombre_firmado


def firmar_archivo2(contenido, llave_privada):
    # Firmar el contenido del archivo
    print("Firmando el contenido del archivo.")
    firma = llave_privada.sign(
        contenido,
        ec.ECDSA(hashes.SHA256())
    )
    print(firma)


    # Crear un nuevo archivo que contenga la firma
    nombre_firmado = f"{"test"}_firmado"
    with open(nombre_firmado, 'wb') as archivo_firmado:
        archivo_firmado.write(firma)
    #antes nombrefirmado
    return firma

