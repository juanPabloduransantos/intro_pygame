# ejemplo de un cuadrado que se mueve

import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  
        self.image.fill((0, 255, 0)) 
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.x += 5 


pygame.init()
pantalla = pygame.display.set_mode((800, 600))
todos_los_sprites = pygame.sprite.Group()

jugador = Jugador(100, 100)
todos_los_sprites.add(jugador)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    todos_los_sprites.update() 
    pantalla.fill((0, 0, 0))  
    todos_los_sprites.draw(pantalla) 
    pygame.display.flip()  
    reloj.tick(60)  

pygame.quit()