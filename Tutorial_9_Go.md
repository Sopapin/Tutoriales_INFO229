# Tutorial de como instalar Go en Ubuntu 18.04  

Go (Golang) es un lenguaje de programación concurrente y compilado inspirado en C, python y C++;
Es desarrollado por Google y principalmente se diseñó para tener una compilación
rápida, facilidad de programación y una ejecución eficiente en producción a la vez. Este 
lenguaje es adecuado de utilizar para programas de sistemas distribuidos o redes.  
Como dato interesante las aplicaciones **Kubernetes** y **Docker** (usada en el curso) son escritas en Go.  
En este tutorial se va a realizar una guía de como instalar Go y hacer un espacio
de trabajo de programación en Go a través de la terminal de Ubuntu 18.04.

## Descargar tarball de Go e instalar

Lo primero que tenemos que realizar es descargar la versión actual de Go verificando desde
su [página oficial](https://golang.org/dl/), nos vamos al apartado de **Linux** y copiamos
del paso 1 la parte del código que esta después de **-xzf**, es decir:  

`tar -C /usr/local -xzf go1.15.6.linux-amd64.tar.gz`    <-- (despues de -xzf)  

A continuación vamos al terminal (asegurandonos de estar en el directorio principal) y anotamos el siguiente código:  

`curl -O https://dl.google.com/go/go1.15.6.linux-amd64.tar.gz`  <-- (despues del segundo "/" se pega lo copiado anteriormente)  

Para verificar el tarball utilizamos `sha256sum` adelante de lo copiado:  

`sha256sum go1.15.6.linux-amd64.tar.gz`  

La salida debe coincidir con `go1.15.6.linux-amd64.tar.gz` para ser válido, si no, se tiene que volver
a descargar el archivo.  

`3918e6cc85e7eaaa6f859f1bdbaac772e7a825b0eb423c63d3ae68b21f84b844  go1.15.6.linux-amd64.tar.gz
`    <-- coincide  

Ahora podremos extraer el archivo descargado con anterioridad de la [página oficial](https://golang.org/dl/) con el comando:  

`sudo tar -xvf go1.15.6.linux-amd64.tar.gz -C /usr/local`  

Debemos ajustar el permiso y dejar que solamente root pueda ejecutar Go para proteger los archivos:  

`sudo chown -R root:root /usr/local/go`  

*PD: No es obligatorio utilizar la ruta /usr/local como predeterminada pero es recomendable.*  

Con estos pasos ya se ha instalado Go en Ubuntu 18.04.  

## Crear un espacio de trabajo en Go  

Los espacios de trabajo de Go contienen dos directorios:  
* **src**: Contiene los archivos de origen de Go (creados por el usuario en lenguaje de programación Go)
El compilador transforma estos archivos para crear un archivo binario ejecutable.
* **bin**: Contiene los ejecutables creados al compilar con las herramientas de Go.  

Para crear un espacio de trabajo nos situamos (recomendablemente) en la ubicación **$HOME/go**:  

`mkdir -p $HOME/go/{bin,src}`  

Se debe configurar el **$GOPATH** para poder utilizar todas las herramientas de Go y de terceros. 
Primero abrimos `~/.profile` con el editor que estime conveniente:  

`nano ~/.profile`  

Ahora se agrega al final del archivo las siguientes líneas:  

~~~
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin:/usr/local/go/bin
~~~

Actualizamos la terminal para cargar las variables globales:  

`. ~/.profile`  

Ahora que se estableció la variable de entorno **$GOPATH** y el root del espacio de trabajo, se puede
utilizar como ejemplo *github.com* como repositorio siguiendo estas estructuras:  

`$GOPATH/src/github.com/username/project`  

Para poder ver los proyectos disponibles se utiliza la herramienta `go get`:  

`go get github.com/username/project`  

Con estos pasos se crearía un espacio de trabajo en Go.  

## Ejemplo de programa en Go  

Crearemos un "Hello World!" para comprender mejor el funcionamiento de Go.  

Se crea el archivo:  

`nano helloworld.go`  

Escribimos el programa en el archivo recién creado:  

```
package main
import "fmt"

func main() {
    fmt.Println("Hello World!")
}
```
Ahora ejecutaremos el programa:  

`go run helloworld.go`

*Salida:*  

`Hello World!`  

Con este programa se termina el tutorial de Go, teniendo el espacio de trabajo creado,
un ejemplo de programa y las configuraciones iniciales.

**Para más información acerca del lenguaje consultar la [Documentación oficial](https://golang.org/doc/code.html)**.
