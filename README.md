# Estructura de un juego en Pygame

## inicializacion

- Como en todo programa en python, se debe importar los modulos o librerias a utilizar
`import pygame`

- Inicializar pygame usando la funcion init (). Inicializa todos los modulos de pygame importados.
`pygame.init()`

## Visualizacion de la ventana

`ventana = pygame.display.set_mode((600, 400))`

- set_mode() es la funcion encargada de definir el tamaño de la ventana. En el ejemplo se esta definiendo una pantalla de 600 px de ancho, por 400 px de alto.

`pygame.display.set_caption("mi ventana")`

- set_caption es la funcion que añade un titulo a la aventana.

### funcion set_mode()

`set_mode(size =(0,0), flags = 0, depth = 0, display = 0)`

- size = (600,400) define el tamaño de la ventana

- flags: define uno o mas comportamientos para la ventana.
    - Valores:
        - pygame.FULLSCREEN
        - pygame.RESIZABLE
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame.
        RESIZABLE: pantalla completa
        dimensiones modificables.

## Bucle del juego - game loop
- Bucle infinito que se interrumpira al cumplir ciertos criterios
- reloj interno del juego
- en cada interaccion del bucle del juego podemos mover un personaje, o tener en cuenta que un objeto a alcanzado a otro, o que se ha cruzado la linea de llegada, lo que quiere decir que la partida ha terminado.- cada iteracion es una oportunidad para actualizar todos los datos relacionados con el estado actual de la partida.
- en cada iteracion se realisan las siguientes tareas:
    1. Comprobar que no se alcanzan las condisiones de parada, en cullo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteracion actual.
    3. obtener las entradas del sistema, o de interaccion con el jugador.
    4. Actualizar todas las entidades que caracterizan el juego
    5. refrescar la pantalla

    ## Superficies pygame
    - superficie:
          - Elemento geometrico.
          - Linea, poligono, imagen, texto que se muestra en la pantalla.
          - El poligono se puede o no rellenar de color.
          - Las superficies se crean de diferentes maneras dependiendo del tipo:
            - imagen: image.load()
            - texto: font.render()
            - Superficie generica: pygame.Surface()
            - Ventana del juego: pygamen.display.set.model()

# Diseño de bandera
!["Bandera_de_colombia"](./screen.jpg)

## gestion del tiempo y los eventos

### Modulo time

- Ofrece varias funciones que permiten cronometrar la sesion actual (desde el init() o pausar), la ejecusion, por ejemplo.
- Funciones
    - pygame.time.get_ticks
    - pygame.time.waitpygame.time.delay

- Ojeto Clock
   - la funcion tick permite actualizar el reloj asociado con el juego actual.
   - Se llama cada vez que se actualiza la pantalla del juego.
   - Permite especificar el numero maximo de fotograma que se muestran por segundo, y por lo tanto, limitar y controlar la velocidad de ejecusion del juego.
   - si insertamos en un bucle de juego la siguiente linea, garantizamos que nunca se ira mas rapido de 58 fotogramas por segundo: `clock.tick(50)`

 ### Gestion de eventos
 - hay diferentes formas para que el programa seppa que se ha desencadenado un evento.
   - es esencial que los programas pueden conocer inmediatamente las acciones del jugador atravez del teclado, el mouse, el joystick o cualquier otro periferico.

   #### Funcion pygame.get
   - permite obtener todos los eventos en espera de ser prosesados y que estan disponibles en unca cola.
   - si no hay ninguno, se obtiene una coleccion vacia.

   ```Python
   # usamos un bucle for para recorrer todos los eventos de la coleccion obtenida de la funcion get.
   for event in pygame.event():
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            PARAR_JUEGO = True
   ```
#### Funcio pygame.event.wait
-esta funcion espera a que ocurra un evento,y en cuanto sucede, esta disponible

```Python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
```


#### Funcion pygame.event.poll
- Devuelve solo uno de los eventos que estan en la cola de espera

  ## Sonidos en Pygame
  - pygame.mixer: modulo que permite la gestion del sonido
  - music: submodulo que gestiona la musica de fondo. necesariamente solo hay uno a la vez
  - Sound: objeto de mixer, que se puede instanciar varias veces para usarlo en los efectos de sonido del juego

  ### Archivos de sonido
  - se recomienda usar dos formatos, principalmente:
      - Formato WAV (Waveform Audio File Format)
      -Formato abierto y gratuito OGG

  ### Channe (canal) en Pygame
  - Un juego tiene varios canales de sonido
  - Se puede asignar un sonido al canal numero 1 y otro diferente al numero 2
  - Entonces es posible reproducir sonidos simultaneamente activando la lectura en diferentes canales

  ## Sprites
  - Objeto que asocia una ubicasion, uan representacion grafica (esta o aquella imagen, por ejemplo) y un conjunto de propiedades.
  - Estas propiedades pueden ser un nombre, un texto, valores booleanos que caracterizan al objeto en cuestion (por ejemplo si el objeto se puede mover o no)
  - Una posible introduccion del termino sprite podria ser " imagen-objeto" que se actualiza con cada iteracion del bucle del juego.
  - cuanto mas complejo es el juego, mas objetos graficos tiene que gestionar y actualizar, lo que puede ser tedioso.
  - pygame usa no solo la nocion de sprite, sino la nocion de grupo de sprites (grupo)
  - la nocion de grupo permite agrupar los objetos del mismo tipo, ejemplo: todos los soldados de un ejercito, lo que se entiende como una coleccion de la instancias de una clase soldado
  - un determinado procesamiento se puede aplicar a un conjunto o subconjunto de sprites por ejemplo cambiar el color de todos los enemigos o hacer invisibles algunos objetos

## Codigo
```Python
# importamos la libreria pygame
import pygame

# iniciaisamos los modulos de pygame
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las direcciones de la ventana
ventana = pygame.display.set_mode((400,400))

# definimos un color
azul = (0,0,255)
rojo = (255,0,0)
amarillo = (255,255,0)
# crear una superficie

azul_superficie = pygame.Surface((400,100))
rojo_superficie = pygame.Surface ((400,100))
amarillo_superficie = pygame.Surface((400,200))
# rellenamos la superficie de azul
azul_superficie.fill((azul))
rojo_superficie.fill((rojo))
amarillo_superficie.fill((amarillo))

# inserto la superficie en la ventana
ventana.blit(azul_superficie, (0,200))
ventana.blit(rojo_superficie, (0,300))
ventana.blit(amarillo_superficie, (0,0))

# actualiza la vision de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()`