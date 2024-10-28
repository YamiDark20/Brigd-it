## Juego Bridg-it

Desarrollar un agente inteligente que juegue BRIDG-IT, contra un usuario. Para ello simulara el ambiente del juego.

## Descripción

El Bridg-it fue inventado por un profesor de la Brown University (EE.UU.), David Gale, a finales de los años 50.

Es un juego de lápiz y papel para dos personas que deben jugar con sendos boligrafos de distintos colores (p.ej. azul y rojo), construyendo inicialmente el "tablero" a base de igual cantidad de puntos de cada color y dispuestos de igual forma a como se ve en la figura, en la que se observa una partida completa en la que el vencedor ha sido el de color azul.

## Indice

* [Reglas Del Juego](#reglas-del-juego)
* [Diagrama de Clases](#diagrama-de-clases)
* [Diagrama de Caso de Usos](#diagrama-de-caso-de-usos)
* [Diagrama de Estados](#diagrama-de-estados)
* [Herramientas](#herramientas)
* [Screenshots](#screenshots)

## Reglas Del Juego

1. Se selecciona el orden de juego (entre el agente y el usuario) y comienza el jugador con la primera jugada. A continuación se van alternando los jugadores en la realización de las jugadas hasta que finaliza el juego.

2. Cada jugada consiste en unir con un trazo cualquier par de puntos, del color correspondiente al jugador, que sean adyacentes horizontal o verticalmente, pero no en diagonal.

3. No está permitido cruzar un trazo ya dibujado en el tablero.

4. El juego finaliza cuando uno de los jugadores consiga construir un camino conexo que una dos lados opuestos del tablero a base de trazos de su color, proclamándose ganador de la partida.

## Diagrama de Clases

![Imagen de diagrama de clase](/media/images/diagrama-clases.png)

## Diagrama de Caso de Usos

![Imagen de diagrama de caso de usos](/media/images/diagrama-caso-uso.png)

## Diagrama de Estados

![Imagen de diagrama de Estados](/media/images/diagrama-estados.png)

## Herramientas

Para el desarrollo del juego se utilizaron las siguientes herramientas:

* **Pygame**: Pygame es una popular biblioteca de Python diseñada para crear juegos y aplicaciones multimedia. Proporciona una interfaz sencilla e intuitiva para trabajar con gráficos, sonido y dispositivos de entrada.

## Screenshots

El juego se jugara con el mouse, donde el jugador sera los puntos rojos. Si intenta seleccionar un punto azul, este no permitira hacer la conexión con otro punto.

### **Juego En Ejecucion**

![Juego En Ejecucion](/media/images/juego-en-ejecucion.png)