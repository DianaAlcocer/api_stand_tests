# Proyecto api_stand_tests - Sp_7

### Pruebas automatizadas para el parámetro "firstName" al crear un usuario

### Descripción

Se automatizaron pruebas exploratorias para el parámetro "firstName" en la solicitud JSON para crear un nuevo usuario, 
empleado su API en Python.

### Contenido

data.py

sender_stand_request.py

configuration.py

create_user_test.py

### Proceso de las pruebas

1. Se modifica el parámetro "name" según el test
2. Se envia la solicitud JSON para crear un nuevo usuario
3. Se recibe una respuesta JSON que puede ser:
   - código 201 y el campo "authToken" con su valor correspondiente.
   - código 400 y el mensaje "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."
   - código 400 y el mensaje "No se han aprobado todos los parámetros requeridos"
4. Se comprueba que el nuevo usuario se haya agregado a la tabla "users"

### Configuración

#### Requisitos

- Variables de entorno:
  - URL_SERVICE (URL del servidor de Urban Grocers)
- Editor de código:
  - _Pycharm_
- Paquetes:
  - _pytest_
  - _requests_
  
#### Instrucciones

1. Clonar o descargar la carpeta del proyecto
2. Abrirla en un editor de código o IDE como _Pycharm_
3. Instalar paquetes _pytest_ y _requests_ desde terminal o en _python packages_
4. Actualizar la url del servidor en _URL_SERVICE_ en el archivo _configuration.py_. No olvides eliminar la última diagonal. 
5. Abrir la terminal y ubicarte en la carpeta del proyecto con el comando _cd <ruta/del/proyecto>_:
    ```sh
    cd projects/api_stand_tests
    ```
6. Ejecuta el comando _pytest_:
    ```sh
   pytest
    ``` 
- El comando _pytest_ ejecutará los archivos que comienzan con test_ o terminan con _test dentro de la ruta 
del proyecto especificada, no distingue entre mayúsculas y minúsculas.
