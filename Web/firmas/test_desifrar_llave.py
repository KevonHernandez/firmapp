from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
import base64


# Funciones que ya tienes en tu archivo utils/criptografia.py
from criptografia import (
    generar_llave_privada,
    convertir_llave_privada_bytes,
    cifrar_llave_privada,
    descifrar_llave_privada,
)

def test_descifrar_llave_privada():
    # Paso 1: Generar la llave privada
    llave_privada_original = generar_llave_privada()

    # Paso 2: Convertir la llave privada a bytes
    llave_privada_bytes = convertir_llave_privada_bytes(llave_privada_original)

    # Paso 3: Cifrar la llave privada con una contraseña

    usuario = Usuario.objects.get(nick="kevon")


    password = "mi_contraseña_segura"
    llave_privada_cifrada, iv_base64, salt_base64 = cifrar_llave_privada(llave_privada_bytes, password)

    # Paso 4: Descifrar la llave privada usando la función descifrar_llave_privada
    llave_privada_descifrada = descifrar_llave_privada(
        base64.b64encode(llave_privada_cifrada).decode('utf-8'),
        usuario.password,
        usuario.iv,
        usuario.salt_llave
    )

    # Paso 5: Comparar las llaves
    llave_privada_descifrada_bytes = convertir_llave_privada_bytes(llave_privada_descifrada)
    assert llave_privada_bytes == llave_privada_descifrada_bytes, "Las llaves no coinciden"

    print("La función descifrar_llave_privada funciona correctamente.")

# Ejecutar el test
if __name__ == "__main__":
    test_descifrar_llave_privada()
