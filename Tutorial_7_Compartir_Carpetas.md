# Tutorial para conectar Ubuntu con Windows para compartir carpetas a través de Samba

En este tutorial veremos como conectar un computador con Sistema Operativo Ubuntu a uno con Windows 10 mediante Wi-Fi.
Microsoft utiliza el protocolo **SMB** para establecer el uso compartido de archivos en Windows, por esto mismo,
para poder conectar computadores de diferentes sistemas operativos usaremos la aplicación **Samba**.

## Instalar Samba en Ubuntu
Primero abriremos una terminal en Ubuntu y agregaremos el siguiente comando para instalar los paquetes:    

`sudo apt-get install samba`  

*PD: El comando utilizado sirve para la mayoría de las versiones de Ubuntu.*

## Verificar conexión de computadores

Necesitamos asegurarnos que ambos equipos se ven a través de la red, por esto tenemos que conseguir la IP
de uno de ellos.  

- En Windows:
  - 1. Pulsamos **Windows + R** al mismo tiempo. Se nos abrirá el programa Ejecutar.
    2. Escribimos **cmd** y pulsamos aceptar.
    3. Se abrirá **Símbolo del sistema**
  - Se escribe el comando **ipconfig**
  - La ip se ubica en la línea **Dirección IPv4**  
  
Luego en Ubuntu escribimos en la terminal el comando:    

    `ping <dirección IP de Windows>`  
    
 Con esto verificamos que funciona y podemos empezar el proceso para compartir carpetas.  
 *PD: Para detener el proceso pulsamos Ctrl + Z.*   
 
 - En Ubuntu:
   - Utilizamos el siguiente comando:  
   `ip a`   
   
   - Se localiza la primera línea en donde diga **link/ether**, asi sabemos la IP del computador en la red principal.
 
 ## Compartir carpeta de Ubuntu a Windows
 1. Creamos una carpeta en el Escritorio (o donde estimes conveniente).
 2. Pulsamos botón derecho sobre la carpeta y pinchamos la opción **Recurso compartido en red local**. Aparecerá una ventana para configurar el uso compartido.
 3. En la ventana pulsamos con un tick las 3 opciones que aparecen.
 4. Pinchamos **Crear compartición** y en la nueva ventana emergente pinchamos **Añadir los permisos automáticamente**  
 
 Con esto la carpeta esta lista para usar y ver los archivos en Windows.  
 
  ## Acceder a carpeta compartida de Ubuntu en Windows   
  Nos vamos a nuestro computador Windows y abrimos el **Explorador de archivos**, en la barra de navegación
  escribiremos la IP de Ubuntu de la siguiente forma:   
  
   `\\<ip de Ubuntu>`  
   
   Al ingresar la dirección automáticamente nos debería aparecer la carpeta compartida y tendremos total acceso a ella.
   
 ## Compartir carpeta de Windows a Ubuntu  
 
 Ahora haremos el proceso inverso, es decir, de Windows compartir una carpeta a Ubuntu.  
 1. Creamos o seleccionamos una carpeta ya creada con el botón derecho.
 2. Elegimos **Propiedades**
 3. En el cuadro que aparece pinchamos **Compartir** y luego **Uso compartido avanzado**
 4. Dentro de **Uso compartivo avanzado** seleccionamos **Compartir esta carpeta** y mas abajo pinchamos **Permisos**.
 5. Dentro de esta ventana activamos todas las casillas **Permitir** (con esto cualquier usuario de otro sistema puede acceder a nuestra carpeta).  
 
 Al terminar estos pasos ya esta creada la carpeta compartida.
 
 ## Acceder a carpeta compartida de Windows a Ubuntu  
 
 Para acceder a una carpeta compartida de Windows a Ubuntu debemos hacer lo siguiente:   
 1. Abrimos el **Explorador de archivos de Ubuntu**
 2. Vamos a **Otras ubicaciones**
 3. Escribimos en el cuadro de la zona inferior que dice **Conectar al servidor** la siguiente ruta de acceso:  
 `smb://<ip del equipo Windows>`   
 4. Pulsamos **Conectar** y nos va a pedir un usuario y contraseña de acceso. (Si no tenemos configurada una contraseña no podemos acceder a la Ubicación de red)  
 
 ## Eliminar restricción de contraseña para carpeta compartida en Windows  
 
 Este paso nos sirve por si no tenemos configurada una contraseña de usuario en Windows.  
 1. Vamos al **botón de inicio de Windows** y cliqueamos con el botón derecho elegiendo la opción de **Conexiones de red**.
 2. En la ventana que abrimos seleccionamos **Centro de redes y recursos compartidos**.
 3. Luego pulsamos **Cambiar configuración de uso compartido avanzado**.
 4. Elegimos la opción **Todas las redes** y al final de la ventana en el apartado **Uso compartido con protección de contraseña** seleccionamos la casilla **Desactivar el uso compartido con protección de contraseña**.
 5. Guardamos cambios.  
 
 Finalmente podemos acceder a nuestra carpeta compartida en Ubuntu sin error al no poseer contraseña de usuario en Windows.  
 Con esto se terminó el tutorial y podemos conectar carpetas desde Ubuntu <-> Windows sin problema alguno y poder compartir nuestra información entre computadores de distintos sistemas operativos sin mayor problema.
