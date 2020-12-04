import pygame
pygame.init()

screen = pygame.display.set_mode([736, 702])
clock = pygame.time.Clock()

done = False

background = pygame.image.load("Mario.jpg").convert()
player = pygame.image.load("iconoaviso.png").convert()
player.set_colorkey([255, 255, 255])

pygame.mouse.set_visible(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_pos = pygame.mouse.get_pos()
    x = mouse_pos[0]
    y = mouse_pos[1]

    screen.blit(background, [0, 0])
    screen.blit(player, [x, y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()