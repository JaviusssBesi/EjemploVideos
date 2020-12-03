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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Color de fondo
    screen.fill(WHITE)

    ###### --- Zona de DIBUJO --- #####

    pygame.draw.circle(screen, BLACK, (400, 100), 25)
    pygame.draw.line(screen, GREEN, [400, 125], [400, 300], 5)
    pygame.draw.line(screen, BLUE, [350, 400], [400, 300], 5)
    pygame.draw.line(screen, BLUE, [450, 400], [400, 300], 5)
    pygame.draw.line(screen, RED, [400, 175], [450, 250], 5)
    pygame.draw.line(screen, RED, [400, 175], [350, 250], 5)



    ###### --- Zona de DIBUJO --- #####


    #Actualizar pantalla
    pygame.display.flip()