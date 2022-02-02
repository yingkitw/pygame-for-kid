import sys, random, pygame

pygame.init()

#4 x 5 board
board = [
	[2,1,1,3],
	[2,1,1,3],
	[4,6,6,5],
	[4,7,8,5],
	[9,0,0,10]
]

class Block2x2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block2x2.png"),(200,200))
		self.rect = pygame.Rect((x,y),(200,200))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

class Block1x2_1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block1x2_1.png"),(100,200))
		self.rect = pygame.Rect((x,y),(100,200))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

class Block1x2_2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block1x2_2.png"),(100,200))
		self.rect = pygame.Rect((x,y),(100,200))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

class Block1x2_3(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block1x2_3.png"),(100,200))
		self.rect = pygame.Rect((x,y),(100,200))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

class Block1x2_4(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block1x2_4.png"),(100,200))
		self.rect = pygame.Rect((x,y),(100,200))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

class Block2x1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block2x1.png"),(200,100))
		self.rect = pygame.Rect((x,y),(200,100))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

class Block1x1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load("rc/block1x1.png"),(100,100))
		self.rect = pygame.Rect((x,y),(100,100))

	def update(self, screen):
	    screen.blit(self.image, self.rect)

def checkCollid(block):
	print(f"right:{block.rect.right},bottom:{block.rect.bottom}")

	if block.rect.left < 0 \
	or block.rect.top < 0 \
	or block.rect.right > 400 \
	or block.rect.bottom > 500:
		return True

	for other in grp:
		if other != block \
		and block.rect.colliderect(other.rect):
			return True
	return False

UP = 1
LEFT = 2
DOWN = 3
RIGHT = 4

def moveBlock(block,direction):
	if direction == LEFT:
		block.rect.x -= 100
		if not checkCollid(block):
			block.rect.x -= 100
			if not checkCollid(block):
				return
			else:
				block.rect.x += 100
			return
		else:
			block.rect.x += 100
	elif direction == RIGHT:
		block.rect.x += 100	
		if not checkCollid(block):
			block.rect.x += 100
			if not checkCollid(block):
				return
			else:
				block.rect.x -= 100
			return
		else:
			block.rect.x -= 100
	elif direction == UP:
		block.rect.y -= 100
		if not checkCollid(block):
			block.rect.y -= 100
			if not checkCollid(block):
				return
			else:
				block.rect.y += 100
			return
		else:
			block.rect.y += 100
	elif direction == DOWN:
		block.rect.y += 100	
		if not checkCollid(block):
			block.rect.y += 100
			if not checkCollid(block):
				return
			else:
				block.rect.y -= 100
			return
		else:
			block.rect.y -= 100

def drawBoard():
	screen.fill((255,255,255))
	grp.update(screen)

def checkWin():
	for block in grp:
		if block is Block2x2\
		and block.rect.left == 100\
		and block.rect.top == 300:
			return True
	return False	


pygame.display.set_caption("华容道")
screen = pygame.display.set_mode((400,500))

grp = pygame.sprite.Group()
grp.add(Block2x2(100,0))
grp.add(Block1x2_1(0,0))
grp.add(Block1x2_2(300,0))
grp.add(Block1x2_3(0,200))
grp.add(Block1x2_4(300,200))
grp.add(Block2x1(100,200))
grp.add(Block1x1(0,400))
grp.add(Block1x1(300,400))
grp.add(Block1x1(100,300))
grp.add(Block1x1(200,300))

currentBlock = None
relx = 0
rely = 0

win_img = pygame.transform.scale(pygame.image.load("rc/win.png"),(200,200))

clock = pygame.time.Clock()
while True:
	clock.tick(10)
	drawBoard()
	if checkWin():
		screen.blit(win_img,(100,100))
	# pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pygame.mouse.get_rel()
			x, y = pygame.mouse.get_pos()
				
			for block in grp:
				if block.rect.collidepoint(x,y):
					relx = x - block.rect.left
					rely = y - block.rect.top
					currentBlock = block
		elif event.type == pygame.MOUSEMOTION:
			if currentBlock != None and pygame.mouse.get_pressed():
				x, y = pygame.mouse.get_pos()
				screen.blit(currentBlock.image,(x-relx,y-rely))
		elif event.type == pygame.MOUSEBUTTONUP:
			xdelta, ydelta = pygame.mouse.get_rel()
			print(f"xdelta:{xdelta}")
			if abs(xdelta) > abs(ydelta) and xdelta > 0:
				moveBlock(currentBlock,RIGHT)
			elif abs(xdelta) > abs(ydelta) and xdelta < 0:
				moveBlock(currentBlock,LEFT)
			elif abs(xdelta) < abs(ydelta) and ydelta > 0:
				moveBlock(currentBlock,DOWN)
			elif abs(xdelta) < abs(ydelta) and ydelta < 0:
				moveBlock(currentBlock,UP)
			currentBlock = None

	pygame.display.update()
		