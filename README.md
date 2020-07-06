[![Build Status](https://travis-ci.com/GabrielEberlein/Bingo.svg?branch=master)](https://travis-ci.com/GabrielEberlein/Bingo)
[![Coverage Status](https://coveralls.io/repos/github/GabrielEberlein/Bingo/badge.svg?branch=master)](https://coveralls.io/github/GabrielEberlein/Bingo?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/GabrielEberlein/Bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/GabrielEberlein/Bingo/?branch=master)
# :fish_cake:Bingo:fish_cake:
Proyecto para la asignatura de Adaptación al Ambiente de Trabajo (ATT) de 6to año informática del Instituto Politécnico Superior (IPS) dada por Mariano Dagostino (Profesor de la especialidad con la barba mas facha). :neckbeard:<br>
El objetivo de este proyecto es acondicionarnos al uso de varias herramientas utilizadas en el ambito informatico al momento de trabajar grandes proyectos en equipos. 

## :hibiscus:Enunciado General:hibiscus:
Usando el lenguaje Python traducimos una funcion que genera cartones de Bingo tradicional. Estos cartones pueden no ser validos por lo que tenemos que escribir tests que nos afirmen cuando lo son.
### Los tests a tener en cuenta son los siguientes:
  - Los números del cartón se encuentran en el rango 1 a 90.
  - Cada columna de un cartón (contando de izquierda a derecha) contiene números que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
  - No hay números repetidos en el cartón.
  - Cada fila de un cartón tiene exactamente 5 celdas ocupadas.
  - Cada cartón es una matriz de 3 x 9.
  - Cada cartón tiene 15 celdas ocupadas.
  - Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
  - Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
  - No pueden existir columnas vacías.
  - No pueden existir columnas con sus tres celdas ocupadas.
  - Cada cartón debe tener 3 y solo 3 columnas con solo una celda ocupada.
  - En una fila no existen más de dos celdas vacías consecutivas.
  - En una fila no existen más de dos celdas ocupadas consecutivas.

## :white_flower:Uso:white_flower:
### Descarga
Podes descargar el zip del repositorio o escribir este comando desde tu consola para clonarlo:
```
git clone https://github.com/GabrielEberlein/Bingo.git
```
### Ejecucion
Para ejecutar el programa debes escribir el siguiente comando:
```
python imprimir_carton.py
```
Aclaración: En distros basadas en `Debian`, se debe ejecutar el programa usando `python3` en lugar de `python`, para usar la version 3.x del mismo.
### Resultado
El programa deberia devolver un carton valido como el siguiente:
```
[0, 17, 23, 0, 0, 51, 0, 75, 84]
[5, 0, 25, 0, 0, 54, 0, 77, 86]
[7, 18, 0, 38, 46, 0, 60, 0, 0]
```
Aclaracion: Los 0 son celdas vacias del carton.



