====================
Guía de Instalación
====================

Entorno de Desarrollo
=====================================

1.- Crear un entorno virtual (python3)

    virtualenv -p python3 <name_virtualenv>

2.- Activar el entorno virtual, ubicarse en la ruta del entorno virtual y realizar el siguiente paso:
    a) Windows

    b) Linux o Mac
        source <name_env>/bin/activate

3.- Acceder a la ruta del proyecto y instalar las dependencias con el comando:
    pip install -r requirements.txt

4.- Verificar el settings.py para su conexion a la base de datos.
