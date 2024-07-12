# Space Invaders

![banner-space](https://github.com/user-attachments/assets/bb0501dd-59d3-4573-bf2f-1ea9bac765a4)


## Sobre el desarrollo

Este juego fue desarrollado como uno de los proyectos finales del **Bootcamp 100 Days of Code** impartido por Angela Yu en el que se pedía construir el juego Space Invaders.
Para su desarrollo y tras analizar diferentes librerías, he decido utilizar ***Pygame*** por ser una librería pensada para la creación de videojuegos en 2D.

### Archivos
- **main.py**: archivo principal desde el cual debe ejecutarse el juego. Controla la pantalla, crea los objetos como la nave, los aliens, las balas y la puntuación y llama a las funciones de las clases. Mantiene la ventana abierta hasta el que jugador decide finalizar
la partida.
- **constants.py**: almacena los valores de las variables constantes que son utilizadas en los módulos.
- **ship.py**: módulo que crea la nave del jugador y controla el movimiento.
- **alien.py**: módulo que dibuja los aliens y controla los movimientos.
- **bullet.py**: módulo que dibuja las balas tando del jugador como de los aliens.
- **score.py**: módulo que actualiza la puntuación del jugador y el nivel. También almacena la puntución más alta alcanzada dentro de un archivo "score.txt", si al inicio de la partida el archivo no existe lo crea. Cuando se inicie de nuevo la partida,
mostrará la máxima puntución que tiene guardada y la modificará si ésta es superada.
- **explosion.py**: se ejecuta cuando una bala colisiona contra un alien o contra la nave, muestra la explosión que consiste en una secuencia de 4 imágenes.
- carpeta **assets**: contiene un directorio denominado **img** con todas las imágenes que son utilizadas en el juego.
- **requirements.txt**: librerías requeridas para ejecutar la aplicación.


## Instrucciones de juego

La misión del jugador (la nave) es eliminar todos los aliens de la pantalla. Para ello debe dispararles con la barra espaciadora, se puede mover de derecha a izquierda con las flechas. Si consigue eliminarlos a todos, se sube de nivel, cuanto mayor sea el nivel, 
más rápido se moverán los aliens.

La partida inicia cuando el jugador pulsa *Start*.

![start-space](https://github.com/user-attachments/assets/a8bf48d2-ab54-4820-8397-546bee712e3b)

Los aliens se moverán de derecha a izquierda.

![init-space](https://github.com/user-attachments/assets/31ee41f3-f008-4963-b3b6-0bc789132d7f)

A su vez, los aliens disparan hacia la zona del jugador, éste debe esquivar las balas. Si es alcanzado por algún disparo tiene un total de 3 oportunidades para seguir jugando.

![game-space](https://github.com/user-attachments/assets/f47175c2-fa3b-4a6f-a6f5-de42c677a74a)


Cuando el jugador consume todas sus vidas (3), la nave explota y aparece la pantalla final en la que se
muestran dos botones:
- *Restart*: inicia una nueva partida desde el nivel 1 y con 0 puntos.
- *Exit*: sale de la aplicación.

![game-over-space](https://github.com/user-attachments/assets/b5eabfdf-0f66-4906-a33b-1903944122b2)


## Requerimientos
Es necesaria la librería ***pygame*** para ejecutar el juego.




