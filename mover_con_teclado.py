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

#Coordenadas del cuadrado
coord_x = 10
coord_y = 10

#Velocidad
x_speed = 0
y_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Eventos Teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_DOWN:
                y_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0

    screen.fill(WHITE)

    coord_x += x_speed
    coord_y += y_speed

    ###### --- Zona de DIBUJO --- #####

    pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100))

    ###### --- Zona de DIBUJO --- #####


    #Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)