from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature


def verificar_firma(archivo, firma, llave_publica):
    try:
        llave_publica.verify(
            firma,
            archivo,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
            print("La firma no es válida. Verifique que el archivo y la firma correspondan a la clave pública proporcionada.")
            return False
    except Exception as e:
            print(f"Error inesperado al verificar la firma")
            return False
