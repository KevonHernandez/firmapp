# Firmapp

**Firmapp** es una aplicación que ofrece a los usuarios la capacidad de firmar digitalmente documentos y verificar esas firmas de manera segura. La plataforma está diseñada para empresas y personas que requieren una solución segura y confiable para la autenticación de documentos digitales sin almacenar los archivos en el servidor, garantizando la privacidad y la integridad de la información.

## Introducción

En la era digital, la necesidad de firmar y verificar documentos electrónicamente es cada vez más común. **Firmapp** proporciona una solución simple pero segura para esta necesidad, permitiendo a los usuarios proteger sus documentos y verificar la autenticidad de los documentos firmados por otros. La seguridad de la aplicación es una prioridad, asegurando que todas las operaciones relacionadas con la firma y verificación de documentos sean confiables y seguras.

## Requisitos Funcionales

### Registro de Usuario
- Los usuarios pueden crear una cuenta proporcionando la información necesaria.

### Inicio de Sesión
- Los usuarios pueden entrar a la plataforma mediante su nombre de usuario y contraseña.

### Firma de Archivos
- Al entrar, el usuario puede subir un archivo a la plataforma y obtener un archivo con la firma digital correspondiente. 
- El archivo original no se almacena en el servidor.

### Verificación de Firma de Archivos
- Los usuarios pueden verificar la validez de un archivo y su firma digital proporcionada por otros usuarios.

## Requisitos No Funcionales de Seguridad

### Almacenamiento Seguro de Información
- Las contraseñas se almacenan de forma segura.
- Las llaves privadas se almacenan cifradas en el servidor usando un algoritmo de cifrado simétrico fuerte (AES).

### Política de Contraseñas
Una política de contraseñas fuerte es crucial para proteger las cuentas de usuario de posibles ataques de fuerza bruta y accesos no autorizados. Por ello, se implementa la siguiente política de contraseñas en **Firmapp**:
- La longitud debe ser al menos de 6 caracteres.
- La longitud no debe superar los 20 caracteres.
- Debe contener al menos un número.
- Debe contener al menos una letra mayúscula.
- Debe contener al menos una letra minúscula.
- Debe contener al menos uno de los siguientes símbolos: `$`, `@`, `#`, `%`.

Estas reglas aseguran que las contraseñas sean lo suficientemente complejas para dificultar su descifrado, incrementando así la seguridad general de la plataforma.

### Medidas contra Ataques Comunes
- Se implementaron medidas de seguridad para proteger contra:
  - Inyección SQL
  - Cross-Site Scripting (XSS)
  - Cross-Site Request Forgery (CSRF)
  - Directory Traversal

---
