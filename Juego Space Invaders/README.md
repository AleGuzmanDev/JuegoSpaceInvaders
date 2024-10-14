
# Space Invaders con Pygame

Este es un sencillo juego de **Space Invaders** hecho con Python y la librería **Pygame**. El jugador controla una nave espacial que puede moverse de izquierda a derecha y disparar láseres para eliminar enemigos. A medida que los enemigos son destruidos, se generan explosiones y se incrementa la puntuación.

## Características
- **Movimiento de la nave**: Mueve tu nave usando las teclas de flecha izquierda y derecha.
- **Disparar**: Usa la barra espaciadora para disparar láseres.
- **Enemigos**: Aparecen continuamente desde la parte superior y se mueven hacia abajo.
- **Explosiones**: Cada vez que destruyes un enemigo, se genera una animación de explosión.
- **Puntuación y vida**: La puntuación aumenta por cada enemigo destruido. El jugador tiene una barra de vida que disminuye al ser golpeado por enemigos o sus balas.
- **Pausa**: Presiona `P` para pausar el juego.

## Requisitos

Antes de ejecutar el juego, asegúrate de tener **Python** y **Pygame** instalados.

### Instalación de Pygame
Para instalar **Pygame**, ejecuta el siguiente comando:
```bash
pip install pygame
```

## Cómo ejecutar el juego

1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de que los archivos de imágenes, sonidos y las carpetas `imagenes/` y `explosion/` estén en el mismo directorio que el script principal.
3. Ejecuta el script principal con Python:
```bash
python space_invaders.py
```

## Controles del Juego

- **Flechas izquierda/derecha**: Mover la nave.
- **Barra espaciadora**: Disparar.
- **P**: Pausar el juego.
- **Enter**: Iniciar el juego en el menú principal o reiniciar tras el `Game Over`.

## Estructura del Proyecto

```
.
├── imagenes/
│   ├── A1.png        # Imagen de la nave del jugador
│   ├── E1.png        # Imagen de los enemigos
│   ├── B1.png        # Imagen de las balas enemigas
│   ├── B2.png        # Imagen de las balas del jugador
│   └── fondo.png     # Imagen de fondo del juego
├── explosion/
│   ├── 1.png         # Imagen de la explosión (frame 1)
│   ├── 2.png         # Imagen de la explosión (frame 2)
│   └── ...           # Más frames de la animación de explosión
├── laser.wav         # Sonido del disparo láser
├── explosion.wav     # Sonido de explosión
├── golpe.wav         # Sonido de impacto del jugador
└── space_invaders.py # Código principal del juego
```

## Funcionamiento

- **Nave del jugador**: Se mueve horizontalmente y dispara hacia arriba.
- **Enemigos**: Descienden desde la parte superior de la pantalla y reaparecen al ser destruidos.
- **Explosiones**: Aparecen en el lugar donde un enemigo es destruido.
- **Colisiones**: Si una bala enemiga golpea al jugador, pierde vida. Si su vida llega a 0, el juego termina.

