
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


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

