from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives.serialization import load_pem_public_key

def verificar_firma(archivo, firma, llave_publica):
    try:
        llave_publica.verify(
            firma,
            archivo,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        print(f"Error al verificar la firma: {e}")
        return False
