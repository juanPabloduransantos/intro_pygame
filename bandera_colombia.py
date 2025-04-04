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

pygame.quit()