import pygame
import sys

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro =  (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
naranja = (255,165,0)
cian = (0,255,255)
gris = (127,127,127)
negro2 = (50,50,50)
piel = (245,200,100)
cafe = (111,78,55)

pygame.init()
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dibujo")
clock = pygame.time.Clock()

rueda_quieta = 0
direccion = 1

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    rueda_quieta += direccion
    if rueda_quieta > 3 or rueda_quieta < -3:
        direccion *= -1

    ventana.fill(rojo)
    pygame.draw.rect(ventana, cian, (50,100,400,350))
    pygame.draw.rect(ventana, negro2, (250,145,160,125))
    pygame.draw.rect(ventana, blanco, (280,170,100,75))
    pygame.draw.circle(ventana, piel, (330,206), 40)
    pygame.draw.circle(ventana, blanco, (315,200), 10)
    pygame.draw.circle(ventana, blanco, (345,200), 10)
    pygame.draw.circle(ventana, cafe, (345,200), 5)
    pygame.draw.circle(ventana, cafe, (315,200), 5)
    pygame.draw.circle(ventana, rojo, (330,225), 10)
    pygame.draw.line(ventana, amarillo,(313,170),(325,190), 5)
    pygame.draw.line(ventana, amarillo,(350,170),(335,190), 5)
    pygame.draw.circle(ventana, gris, (120,330), 55)
    pygame.draw.rect(ventana, gris, (150,270,280,130))
    pygame.draw.rect(ventana, negro2, (135,285,15,100))
    pygame.draw.rect(ventana, negro2, (100,260,40,150))

    pygame.draw.circle(ventana, negro2, (200 + rueda_quieta,410), 40)
    pygame.draw.circle(ventana, negro2, (300 + rueda_quieta,410), 40)
    pygame.draw.circle(ventana, negro2, (400 + rueda_quieta,410), 40)

    pygame.draw.rect(ventana, negro, (209 + rueda_quieta,395,80,30))
    pygame.draw.rect(ventana, negro, (309 + rueda_quieta,395,80,30))

    pygame.draw.rect(ventana, gris, (238,130,180,20))
    pygame.draw.rect(ventana, gris, (260,115,140,20))
    pygame.draw.rect(ventana, negro2, (160,220,60,50))
    pygame.draw.rect(ventana, negro2, (150,200,80,30))
    
    fuente_arial = pygame.font.SysFont("Arial", 26, 2, 1)
    texto0 = fuente_arial.render("Carrillo", 1, negro)
    texto = fuente_arial.render("Colegio san jose del guanenta", 1, negro)
    texto2 = fuente_arial.render("Sistemas 2", 1, negro)
    texto3 = fuente_arial.render("Juan Pablo Duran Santos", 1, negro)
    ventana.blit(texto,(52,10))
    ventana.blit(texto2,(180,50))
    ventana.blit(texto3,(0,470))
    ventana.blit(texto0,(200,325))

    pygame.display.flip()
