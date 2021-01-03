# Tutorial de como instalar y proteger Redis

Redis(Remote Dictionary Server) es un sistema de almacenamiento de estructuras de datos 
clave-valor en memoria y de código abierto, permite su uso como base de datos, caché o 
agente de mensajes y cola. Es conocido y utilizado por su flexibilidad,
rendimiento y su soporte en varios idiomas, por esto mismo es el almacén de valores de clave
más popular en la actualidad.  
Ahora en este tutorial se verá como instalar y configurar Redis en un computador con Ubuntu 18.04.  

## Instalación y configuración de Redis  
Primero abriremos una terminal en Ubuntu y agregaremos el siguiente comando para actualizar 
los paquetes:    

`sudo apt update`  

Luego se ingresará el siguiente comando para instalar Redis:

`sudo apt install redis-server`  

Con este comando quedará instalado Redis y sus dependencias. Pero es necesario cambiar 
cierta configuración, para esto se abre el archivo generado autmáticamente con el comando:  

`sudo nano /etc/redis/redis.conf`    
 *
*PD*: Puede utilizar el editor que prefiera.*  

Ahora hay que encontrar la orden **supervised** en el archivo y cambiar el **no** por **systemd**, esto
con el propósito de tener un mayor control sobre su funcionamiento.
```
# If you run Redis from upstart or systemd, Redis can interact with your
# supervision tree. Options:
#   supervised no      - no supervision interaction
#   supervised upstart - signal upstart by putting Redis into SIGSTOP mode
#   supervised systemd - signal systemd by writing READY=1 to $NOTIFY_SOCKET
#   supervised auto    - detect upstart or systemd method based on
#                        UPSTART_JOB or NOTIFY_SOCKET environment variables
# Note: these supervision methods only signal "process is ready."
#       They do not enable continuous liveness pings back to your supervisor.
supervised systemd
```  
Luego de modificarlo, se guarda el archivo y reiniciamos Redis para que se apliquen los cambios.  
 
 `sudo systemctl restart redis.service`   
 
Con esto ya quedará instalado y configurado Redis. Se puede verificar su funcionamiento con:  
 
 `sudo systemctl status redis`  
 
 Si el comando anterior funciona correctamente el resultado sería el siguiente:  
 ```
 redis-server.service - Advanced key-value store
   Loaded: loaded (/lib/systemd/system/redis-server.service; enabled; vendor pre
   Active: active (running) since Sat 2021-01-02 22:26:47 -03; 13min ago
     Docs: http://redis.io/documentation,
           man:redis-server(1)
 Main PID: 26059 (redis-server)
    Tasks: 4 (limit: 4036)
   CGroup: /system.slice/redis-server.service
           └─26059 /usr/bin/redis-server 127.0.0.1:6379
. . .
 ```  
 
## Funcionamiento de Redis  
Para comprobar el correcto funcionamiento de Redis establezcamos una conexión con el servidor
utilizando un cliente de línea de comandos:

`redis-cli`  

Realizamos una prueba de conectividad con el comando *ping*:  

`ping`  

*Salida:*  

`PONG`  

Con esta salida se comprueba que la conexión con el servidor está activa.  
Nos podemos asegurar de configurar las claves ejecutando:  

`set test "Esto es un ejemplo!"`  

*Salida:*  

`OK`  

Se puede recuperar el valor con el siguiente comando:  

`get test`  

*Salida:*  

`"Esto es un ejemplo!"`

Si devuelve lo mismo que se escribió, se confirma que se puede obtener el valor por lo que
podemos cerrar el programa con:  

`exit`  

Y como última prueba vamos a revisar si Redis persiste los datos aún despues de detenerse o reiniciarse.
Para esto lo reiniciaremos:  

`sudo systemctl restart redis`  

Se establece la conexión con el cliente:  

`redis-cli`  

`get test`  
 
 *Salida:*  
 
 `"Esto es un ejemplo!"`  
 
 Por lo tanto se comprueba la persistencia de datos y el correcto funcionamiento.   

Finalmente a través de este tutorial se realizó una correcta instalación y configuración de 
Redis, comprobando su funcionamiento y su persistencia de datos. 
