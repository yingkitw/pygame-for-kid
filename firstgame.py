import pygame
     
pygame.init()

pygame.display.set_caption("豆豆的马里奥")

screen = pygame.display.set_mode((400,300))

image = pygame.image.load("mario.png")

running = True

xpos = 0
ypos = 0

while running:
	xpos += 1
	# ypos += 1

	screen.fill((0,0,0))
	screen.blit(image, (xpos,ypos))

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			xpos, ypos = pygame.mouse.get_pos()
     