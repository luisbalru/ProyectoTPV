# Proyecto IV
[![Build Status](https://travis-ci.org/joseviro/ProyectoTPV.svg?branch=master)](https://travis-ci.org/joseviro/ProyectoTPV)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Terminal punto de venta (TPV)
Repositorio creado para el proyecto (**personal**) de la asignatura Infraestructura Virtual de 4º del Grado de Ingeniería Informática (UGR - TIC).

En este proyecto voy a realizar una TPV para la gestión de ventas en el ambito hostelero, concretamente restaurantes y bares.

He decidido realizar este microservicio por la intima relación que poseo desde hace pocos años con este sector y para en un futuro abordar el proyecto al completo.

## Herramientas

- El lenguaje de programación que voy a utilizar es python.
- El framework que utilizaré es flask.
- Los tests los realizaré con la biblioteca unittest.
- La base de datos que utilizaré es MariaDB (ya usada en otras asignaturas) para actualizar los cambios en el nivel de existencias de mercancías (STOCK).

## Instalando lo necesario
pip install -r requirements.txt

## Para ejecutar los tests
pytest

## Para ejecutar
python3 pruebas.py

## Uso
El uso de estos métodos es para llevar a cabo el control de las mesas, cuentas, stock y ganancias diarias del restaurante o bar en cuestión. 

## Por qué he elegido estas herramientas de test e integración continua:
[Aquí](https://joseviro.github.io/ProyectoTPV/docs/explicacionElecciones)

## PaaS Elegido: Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

He elegido heroku porque es gratuito y la documentación que aporta es muy intuitiva.
**despliegue** : [proyectoTPV](https://stark-hollows-36939.herokuapp.com)
