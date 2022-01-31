from cmath import rect
from email.headerregistry import Group
import sys, random, pygame

pygame.init()

#4 x 4 board
board = [
	[2,1,1,3],
	[2,1,1,3],
	[4,6,6,5],
	[4,7,8,5],
	[9,0,0,10]
]

block2x2 = 1
block1x2_1 = 2
block1x2_2 = 3
block1x2_3 = 4
block1x2_4 = 5
block2x1 = 6
block1x1_1 = 7
block1x1_2 = 8
block1x1_3 = 9
block1x1_4 = 10

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

def moveBlock(block):
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

def updateBoard(x,y):
	# if board[y][x] == block2x2:
	# 	if board[y-1][x] == 0:
	# 	board[y-1][x] 
	pass

def drawBoard():
	screen.fill((255,255,255))
	grp.update(screen)


	# done = []
	# for i in range(5):
	# 	for j in range(4):
	# 		if board[i][j] > 0 and board[i][j] not in done:
	# 			screen.blit(block_img_map[board[i][j]],(j*100,i*100))
	# 			done.append(board[i][j])
	# 		else:
	# 			pass

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

block2x2_img = pygame.transform.scale(pygame.image.load("rc/block2x2.png"),(200,200))
block1x2_1_img = pygame.transform.scale(pygame.image.load("rc/block1x2_1.png"),(100,200))
block1x2_2_img = pygame.transform.scale(pygame.image.load("rc/block1x2_2.png"),(100,200))
block1x2_3_img = pygame.transform.scale(pygame.image.load("rc/block1x2_3.png"),(100,200))
block1x2_4_img = pygame.transform.scale(pygame.image.load("rc/block1x2_4.png"),(100,200))
block2x1_img = pygame.transform.scale(pygame.image.load("rc/block2x1.png"),(200,100))
block1x1_img = pygame.transform.scale(pygame.image.load("rc/block1x1.png"),(100,100))

block_img_map = {block2x2:block2x2_img,
	block1x2_1:block1x2_1_img,
	block1x2_2:block1x2_2_img,
	block1x2_3:block1x2_3_img,
	block1x2_4:block1x2_4_img,
	block2x1:block2x1_img,
	block1x1_1:block1x1_img,
	block1x1_2:block1x1_img,
	block1x1_3:block1x1_img,
	block1x1_4:block1x1_img,
	}

while True:
	drawBoard()
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			x, y = pygame.mouse.get_pos()
			
			for block in grp:
				if block.rect.collidepoint(x,y):
					moveBlock(block)
		