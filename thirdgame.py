import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((1000,1000))
font = pygame.font.Font(None,30)
y = 0
x = 0

while True:
	screen.fill((255,255,255))
	y = y + 1
	text = font.render("hello",True,(255,0,0))
	screen.blit(text,(x,y))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			x,y = pygame.mouse.get_pos()