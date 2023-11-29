# Juego de Tomás Mugetti
## Trabajo práctico para el tutor - Kodland - 29/11/2023



### Gameplay
El juego consiste en un jugador (circulo verde) que debe esquivar enemigos (cuadrados rojos) mientras recolecta monedas (circulos amarillos).

El jugador puede moverse utilizando las flechas del teclado.

La partida finaliza cuando el jugador colisiona con un enemigo.

### Funcionalidad
El programa cuenta con *managers* que se encargan de manejar las distintas clases del programa. Siendo estas el jugador, las monedas, y los enemigos. Además hay otros *managers* que se encargan de detectar colisiones, y manejar los estados de la aplicación.

Además, existe un archivo *Definitions.py* que contiene las definiciones de diferentes variables del juego, para poder ser ajustadas las mismas de manera sencilla y clara.


### UX - flow

El jugador es bienvenido por una pantalla de inicio, donde puede comenzar a jugar apretando la barra espaciadora, o salir de la aplicación apretando la tecla escape.

Una vez comenzada la partida, el jugador puede apretar espace para acceder al menu de pausa.

Dentro del menú de pausa el jugador puede resumir su partida utilizando la barra espaciadora, o salir de la aplicación apretando la telca escape.

Al finalizar la partida, se muestra al jugador su puntaje. Desde aquí puede comenzar una partida nueva apretando la barra espaciadora, o salir de la aplicación apretando la tecla escape.