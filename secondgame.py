from email.mime import image
import pygame
pygame.init()
screen = pygame.display.set_mode((600,800))
image = pygame.image.load("mario.png")
x =0
y=50
running = True
while running:
	x=x+1
	screen.fill((0,0,0))
	screen.blit(image,(x,y))
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()