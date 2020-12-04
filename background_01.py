import pygame
pygame.init()

screen = pygame.display.set_mode([736, 702])
clock = pygame.time.Clock()

done = False

background = pygame.image.load("Mario.jpg").convert()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, [0, 0])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()