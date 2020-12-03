import pygame, sys
pygame.init()

#Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 500)

#Crear ventana
screen = pygame.display.set_mode(size)

#Controlar FPS
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]
    screen.fill(WHITE)

    ###### --- Zona de DIBUJO --- #####

    pygame.draw.rect(screen, RED, (x, y, 100, 100))

    ###### --- Zona de DIBUJO --- #####


    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)