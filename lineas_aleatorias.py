import pygame
import sys
import math
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro =  (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
PI = math.pi

numero_lineas = 100

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Dibujar formas con pygame")

clock = pygame.time.Clock()


while 1:
    clock.tick(50)

   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            sys.exit()

   
    ventana.fill(naranja)

    pygame.draw.rect(ventana, negro, ((50,100), (400,350)), 1)

    fuente_arial = pygame.font.SysFont("Arial", 26, 2, 1)
    texto = fuente_arial.render("Colegio san jose del guanenta", 1, negro)
    texto2 = fuente_arial.render("Sistemas 2", 1, negro)
    texto3 = fuente_arial.render("Juan Pablo Duran Santos", 1, negro)
    ventana.blit(texto,(52,10))
    ventana.blit(texto2,(180,50))
    ventana.blit(texto3,(0,470))

    for i in range(numero_lineas):
   
        linea1 = random.randint(50, 50 + 400)
        linea2 = random.randint(100, 100 + 350)
        linea3 = random.randint(50, 50 + 400)
        linea4 = random.randint(100, 100 + 350)
        
        color_linea = random.choice([rojo, azul, verde, rosado, amarillo, naranja, cian])

        pygame.draw.line(ventana, color_linea, (linea1, linea2), (linea3, linea4))
        
    pygame.display.flip()
