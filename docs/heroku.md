# Heroku [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Instalación:
pre-instalado-> git

$ sudo snap install heroku --classic

## Iniciar sesión ([si no estás registrado](https://signup.heroku.com/))

$ heroku login

## Despliegue

Desde la página web:

- Nombramos nuestra aplicación y elegimos la región:

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/Captura%20de%20pantalla%20de%202018-10-31%2017-10-51.png)

- Conectamos con nuestro repositorio de git

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/Captura%20de%20pantalla%20de%202018-10-31%2017-12-26.png)

- Una vez hemos conectado nuestro repositorio podemos activar la sincronización automática

![img](https://github.com/joseviro/ProyectoTPV/blob/master/docs/img/Captura%20de%20pantalla%20de%202018-10-31%2017-17-54.png)

Desplegamos nuestra aplicación pulsando el boton "DeployBranch" y si todo ha ido correctamente al terminar la operación obtendremos un mensaje de *Your app was successfully deployed.* y el enlace a la aplicación.

Podemos comprobar que está corriendo (al menos una instancia) con:

$ heroku ps:scale web=1

Y para ir a la página web sino hemos copiado el url también podemos ejecutar la siguiente orden desde nuestro repo:

$ heroku open

----------------------------------

### Otras utilidades de heroku

- Ver aplicaciones activas:

$ heroku apps

- Eliminar aplicaciones:

$ heroku apps:destroy

-----------------------------------------------------

## Registros | Logs

- Ver los últimos registros:

heroku logs --tail

-----------------------------------
## Procfile
El motivo para usar un Procfile es para declarar explícitamente qué comando debe ejecutarse para iniciar su aplicación.

El Procfile debe residir en el directorio raíz de su aplicación. No funciona si se coloca en otro lugar.

El archivo Proc es siempre un archivo de texto simple que se nombra Procfile sin una extensión de archivo . *Por ejemplo, Procfile.txt no es válido.*

Formato del archivo:

<process type>: <command>

<process type>es un nombre alfanumérico para su comando, como web, worker, urgentworker, clock, release...

<command> tipo de proceso debe ejecutar en el inicio

Ejemplo:

web: <instrucción shell> -> web: python app.py ó cd src && python app.py

Le está diciendo a heroku que cuando realice el proceso web debe realizar el comando establecido.


### PROBLEMA
Los marcos web de Django y Flask cuentan con servidores web incorporados convenientes, pero estos servidores de bloqueo solo procesan una sola solicitud a la vez. Si implementa con uno de estos servidores en Heroku, sus recursos dinámicos serán subutilizados y su aplicación no se responderá.

**Solución**: Gunicorn: Nos permite servir nuestra aplicación Flask con múltiples workers para incrementar el rendimiento de nuestra aplicación.

web: gunicorn <nombre_del_archivo_python sin extension>:app --log-file -
