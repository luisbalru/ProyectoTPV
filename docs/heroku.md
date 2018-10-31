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
