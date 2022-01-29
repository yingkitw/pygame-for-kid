import sys,pygame,random
pygame.init()
jrhsi = pygame.display.set_mode((1500,1000))
red = 0
green = 0
blue = 0
mario = pygame.image.load("mario.png")
mariox = 0
marioy = 0 
while True:
	mariox+=1
	marioy+=2
	jrhsi.fill((red,green,blue))
	jrhsi.blit(mario,(mariox,marioy))
	pygame.display.update()
	for vr in pygame.event.get():
		if vr.type == pygame.QUIT:
			sys.exit()
		elif vr.type == pygame.MOUSEBUTTONUP:
			red = random.randint(0,255)
			green = random.randint(0,255)
			blue = random.randint(0,255)
			mariox,marioy = pygame.mouse.get_pos()