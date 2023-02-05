import pygame  

pygame.init()

screan = pygame.display.set_mode((600,400))
pygame.display.set_caption('Classify')
running=True
Green=(255,255,255)
clock = pygame.time.Clock()

while running:
    clock.tick(60)       
    screan.fill(Green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()