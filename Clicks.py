import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:

     
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


  screen.fill((173, 216, 230))


  pygame.draw.circle(screen, (0, 0, 255), (250, 290), 75)


  pygame.display.flip()


pygame.quit()
