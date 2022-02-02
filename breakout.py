import sys, pygame, random, pygame.sprite

class Ball(pygame.sprite.Sprite): 
	def __init__(self):
	    	pygame.sprite.Sprite.__init__(self)
	    	self.image = pygame.transform.scale(pygame.image.load("rc/ball.png"),(10,10))
		self.rect = pygame.Rect((x,y),(10,10))

	def update(self):
		screen.blit(self.image, self.rect)

class Bar(pygame.sprite.Sprite):
	def __init__(self):
	    	pygame.sprite.Sprite.__init__(self)
	    	self.image = pygame.transform.scale(pygame.image.load("rc/bar.png"),(10,10))
		self.rect = pygame.Rect((x,y),(100,5))

	def update(self):
		screen.blit(self.image, self.rect)

class Block(pygame.sprite.Sprite):
	def __init__(self):
	    	pygame.sprite.Sprite.__init__(self)
	    	self.image = pygame.transform.scale(pygame.image.load("rc/block.png"),(10,10))
		self.rect = pygame.Rect((x,y),(100,5))

	def update(self):
		screen.blit(self.image, self.rect)

pygame.init()

pygame.display.set_caption("打砖块")
screen = pygame.display.set_mode((500,500))

grp = pygame.sprite.Group()
grp.add(Ball())
grp.add(Bar())

while True:
	screen.fill((255,255,255))
	grp.update()
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()