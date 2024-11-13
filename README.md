# ING-SOFTWARE-2
Trabajo Universidad Libre
--------------------------------------------------------------------------------------------------------------
La gestion de inventarios es una parte crucial de las operaciones empresariales, ya que permite mantener un control riguroso sobre los bienes y y productos, ayudando a optimizar los recursos y mejorando la toma de decisiones. 
--------------------------------------------------------------------------------------------------------------

# Manual de Usuario
Bienvenido al manual de usuario de Gestion de inventarios, este documenta se diseño buscando generar una guia completa de acuerdo al correcto uso de todas sus caracteristicas y funcionalidades, de esta manera facilitando su administracion.

# Requisitos
- Django 5.1
- Navegador Web (Recomendado: Basados en Chromium)
- SQLite3
- Acceso a internet

# Instalacion
1. Comprobar que estan todos los requesisitos instalados
2. Descargar y descomprimir el archivo de Github
3. Dirigirse a la ruta donde se encuentra el archivo manage.py
4. Correr el siguiente comando
   >> Py manage.py migrate
5. Crea super usuario
   >> Py manage.py createsupeuser
6. Correr el servidor
   >> py manage.py runserver
7. Dirigirse a la url que le devuelve django

# Uso de Caja
1. Se loguea el trabajador con su repectiva cedula y contraseña
2. Ingresa a caja
+   Agregar producto a la caja
    1. En el menu desplegable seleciona el producto 
    2. Oprimir el boton agregar
+   Eliminar producto de la caja
    1. En el menu desplegable seleciona el producto
    2. Oprime el boton eliminar
+   Limpiar caja
    1. Oprimir el boton de limpiar
+   Generar el recibo o pago
    1. Una vez agregado el producto en la caja
    2. Oprimir el boton de pago
    3. Se le habra descargado un archivo con la factura
# Uso de Inventario
1. Se loguea el trabajador con su repectiva cedula y contraseña
2. Ingresa a inventario
+   Buscar en inventario
    1. Agregar el ISBN o buscar el producto en la lista desplegable
    2. Oprimir el boton de buscar
+   Editar producto existente
    1. Agregar el ISBN o buscar el producto en la lista desplegable
    2. Oprimir el boton de buscar
    3. En la tabla selecciona editar
    4. Ajustar los datos del producto
    5. Oprimir el boton de 'Guardar cambios'
+   Agregar producto nuevo
    1. Oprimir el boton agregar
    2. Rellenar todos los datos del producto(El descuento del producto es un decimal no un porcentaje '%')
    3. Oprimir el boton enviar
# Uso de proveedor
1. Se loguea el trabajador con su repectiva cedula y contraseña
2. Ingresa a Proveedor
 +  Buscar productos por proveedor
    1. Selecionar el la lista desplegable el proveedor
    2. Oprimir el boton buscar
    3. Se mostrara la lista de producto por proveedor
+  Agregar un nuevo proveedor
    1. Oprimir el boton agregar
    2. Rellenar todos los datos
    3. Oprimir el boton enviar
# Uso de Administrador
1. Se loguea el trabajador con su repectiva cedula y contraseña
2. Ingresa a Administrador
+   Añadir un nuevo usuario
    1. Oprimir el boton añadir
    2. Rellenar con los datos del nuevo usuario y asignar permisos

 
 
       




