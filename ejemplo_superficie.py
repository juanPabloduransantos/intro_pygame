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
# crear una superficie

azul_superficie = pygame.Surface((300,300))

# rellenamos la superficie de azul
azul_superficie.fill((azul))

# inserto la superficie en la ventana
ventana.blit(azul_superficie, (0,0))

# actualiza la vision de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()