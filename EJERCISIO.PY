import pygame
import sys
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
io = (255, 255, 0)
po = (0, 255, 255)
color_aleatorio = (random.randint(rojo,azul,verde,io,po))

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("el cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO_XX = 3
YY = 225 
MOVIMIENTO_YY = 3  

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    
    XX = XX + MOVIMIENTO_XX
    if XX >= 450:
        XX = 450
        MOVIMIENTO_XX = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO_XX = 3


    YY = YY + MOVIMIENTO_YY
    
    if YY >= 450:
        YY = 450
        MOVIMIENTO_YY = -3
    elif YY <= 0:  
        YY = 0
        MOVIMIENTO_YY = 3  

    pygame.draw.rect(ventana, rojo, (XX, 0, 50, 50))  
    pygame.draw.rect(ventana, verde, (XX, 450, 50, 50))  
    pygame.draw.rect(ventana, verde, (0, YY, 50, 50))
    pygame.draw.rect(ventana, io, (450, YY,50,50))
    pygame.draw.rect(ventana, color_aleatorio,(200,200,100,100))

    pygame.display.flip()
