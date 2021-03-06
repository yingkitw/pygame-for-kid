import sys, random, pygame, numpy

BLOCKWIDTH = 30

class Tetris:
	def drawScore(self,screen,font):
		img = font.render(f"{self.score}",True,(255,0,0))
		screen.blit(img,
		((screen.get_width()-img.get_width())/2,
		50))

	def drawGrid(self):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):	
				pygame.draw.rect(screen, (255,255,255), 
				(i*self.blockwidth,j*self.blockwidth,self.blockwidth,self.blockwidth), width=1)

	def drawBlock(self,screen):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				rect = (i*self.blockwidth,j*self.blockwidth,self.blockwidth,self.blockwidth)
				pos = (i*self.blockwidth,j*self.blockwidth)
				#draw droppingBlocks or settleBlocks
				if self.droppingBlocks[i][j] == 1 or self.settleBlocks[i][j] == 1:
					screen.blit(self.purple_img, pos)
				elif self.droppingBlocks[i][j] == 2 or self.settleBlocks[i][j] == 2:
					screen.blit(self.blue_img, pos)
				elif self.droppingBlocks[i][j] == 3 or self.settleBlocks[i][j] == 3:
					screen.blit(self.green_img, pos)
				elif self.droppingBlocks[i][j] == 4 or self.settleBlocks[i][j] == 4:
					screen.blit(self.red_img, pos)
				elif self.droppingBlocks[i][j] == 5 or self.settleBlocks[i][j] == 5:
					screen.blit(self.orange_img, pos)
				elif self.droppingBlocks[i][j] == 6 or self.settleBlocks[i][j] == 6:
					screen.blit(self.yellow_img, pos)
	def checkFullRow(self,rowNo):
		for i in range(self.totalcolumn):
			if self.settleBlocks[i][rowNo] == 0:
				return False
		return True

	def cleanRow(self):
		newblocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		k = self.totalrow-1
		for j in range(self.totalrow-1,-1,-1):
			if not self.checkFullRow(j):
				for i in range (self.totalcolumn):
					newblocks[i][k] = self.settleBlocks[i][j]
				k-=1
			
		self.settleBlocks = newblocks	

	def checkOverlap(self,blocks):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.settleBlocks[i][j] > 0 and  blocks[i][j] > 0:
					return True
				elif blocks[i][j] > 0 and j+1 == self.totalrow:
					return True
		return False

	def settle(self):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0:
					self.settleBlocks[i][j] = self.droppingBlocks[i][j]
					self.droppingBlocks[i][j] = 0
	

	def dropBlock(self):
		newblocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if (j+1)<self.totalrow:
					newblocks[i][j+1] = self.droppingBlocks[i][j]

		if self.checkOverlap(newblocks):
			self.settle()
		else:
			self.droppingBlocks = newblocks

	def fillFull(self):
		for j in range(self.totalrow-1,self.totalrow-3,-1):
			for i in range(self.totalcolumn):
				self.settleBlocks[i][j] = 1

	def canLeft(self):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0:
					if i == 0:
						return False
					elif self.settleBlocks[i-1][j] > 0:
						return False
		return True

	def leftBlock(self):
		if not self.canLeft():
			return
		newblocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0:
					newblocks[i-1][j] = self.droppingBlocks[i][j]

		self.droppingBlocks = newblocks 

	def canRight(self):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0:
					if (i+1) == self.totalcolumn:
						return False
					elif self.settleBlocks[i+1][j] > 0:
						return False
		return True

	def rightBlock(self):
		if not self.canRight():
			return

		newblocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0:
					newblocks[i+1][j] = self.droppingBlocks[i][j]
		self.droppingBlocks = newblocks 

	
	def rotateBlock(self):
		newblocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0 \
				and i>=0 and (i+1)<self.totalcolumn:
					if self.blockType == 1:
						# XX
						# XX
						self.droppingBlocks = newblocks
						return
					elif self.blockType == 2:
						# XXXX
						if self.rotateCount == 0:
							newblocks[i+1][j-1] = 2
							newblocks[i+1][j] = 2
							newblocks[i+1][j+1] = 2
							newblocks[i+1][j+2] = 2
							self.rotateCount = 1
						else:
							newblocks[i-1][j+1] = 2
							newblocks[i][j+1] = 2
							newblocks[i+1][j+1] = 2
							newblocks[i+2][j+1] = 2
							self.rotateCount = 0
						self.droppingBlocks = newblocks
						return
					elif self.blockType == 3:
						#  X
						# XXX
						if self.rotateCount == 0:
							newblocks[i][j-1] = 3
							newblocks[i][j] = 3
							newblocks[i][j+1] = 3
							newblocks[i+1][j] = 3
							self.rotateCount = 1
						elif self.rotateCount == 1:
							newblocks[i][j] = 3
							newblocks[i-1][j+1] = 3
							newblocks[i][j+1] = 3
							newblocks[i+1][j+1] = 3
							self.rotateCount = 2
						elif self.rotateCount == 2:
							newblocks[i][j] = 3
							newblocks[i-1][j+1] = 3
							newblocks[i][j+1] = 3
							newblocks[i][j+2] = 3
							self.rotateCount = 3
						else:
							newblocks[i][j] = 3
							newblocks[i-1][j+1] = 3
							newblocks[i][j+1] = 3
							newblocks[i+1][j+1] = 3
							self.rotateCount = 0
						self.droppingBlocks = newblocks
						return
					elif self.blockType == 4:
						# X
						# XXX
						if self.rotateCount == 0:
							newblocks[i][j] = 4
							newblocks[i+1][j] = 4
							newblocks[i][j+1] = 4
							newblocks[i][j+2] = 4
							self.rotateCount = 1
						elif self.rotateCount == 1:
							newblocks[i][j] = 4
							newblocks[i][j+1] = 4
							newblocks[i][j+2] = 4
							newblocks[i+1][j+2] = 4
							self.rotateCount = 2
						elif self.rotateCount == 2:
							newblocks[i+1][j] = 4
							newblocks[i+1][j+1] = 4
							newblocks[i][j+2] = 4
							newblocks[i+1][j+2] = 4
							self.rotateCount = 3
						else:
							newblocks[i][j] = 4
							newblocks[i][j+1] = 4
							newblocks[i+1][j+1] = 4
							newblocks[i+2][j+1] = 4
							self.rotateCount = 0
						self.droppingBlocks = newblocks
						return
					elif self.blockType == 5:
						#   X
						# XXX
						if self.rotateCount == 0:
							newblocks[i][j] = 5
							newblocks[i][j+1] = 5
							newblocks[i][j+2] = 5
							newblocks[i+1][j+2] = 5
							self.rotateCount = 1
						elif self.rotateCount == 1:
							newblocks[i][j] = 5
							newblocks[i+1][j] = 5
							newblocks[i+2][j] = 5
							newblocks[i][j+1] = 5
							self.rotateCount = 2
						elif self.rotateCount == 2:
							newblocks[i+1][j] = 5
							newblocks[i+1][j+1] = 5
							newblocks[i][j+2] = 5
							newblocks[i+1][j+2] = 5
							self.rotateCount = 3
						else:
							newblocks[i+2][j] = 5
							newblocks[i][j+1] = 5
							newblocks[i+1][j+1] = 5
							newblocks[i+2][j+1] = 5
							self.rotateCount = 0
						self.droppingBlocks = newblocks
						return
					elif self.blockType == 6:
						# XX
						#  XX
						if self.rotateCount == 0:
							newblocks[i+1][j] = 6
							newblocks[i+1][j+1] = 6
							newblocks[i][j+1] = 6
							newblocks[i][j+2] = 6
							self.rotateCount = 1
						else:
							newblocks[i][j+1] = 6
							newblocks[i+1][j+1] = 6
							newblocks[i+1][j] = 6
							newblocks[i+2][j] = 6
							self.rotateCount = 0
						self.droppingBlocks = newblocks
						return

	def addBlockIfNone(self):
		for i in range(self.totalcolumn):
			for j in range(self.totalrow):
				if self.droppingBlocks[i][j] > 0:
					return

		self.blockType = random.randint(1,7)
		self.rotateCount = 0
		if self.blockType == 1:
			# XX
			# XX
			self.droppingBlocks[self.totalcolumn//2][0] = 1
			self.droppingBlocks[self.totalcolumn//2+1][0] = 1
			self.droppingBlocks[self.totalcolumn//2][1] = 1
			self.droppingBlocks[self.totalcolumn//2+1][1] = 1
		elif self.blockType == 2:
			# XXXX
			self.droppingBlocks[self.totalcolumn//2][0] = 2
			self.droppingBlocks[self.totalcolumn//2][1] = 2
			self.droppingBlocks[self.totalcolumn//2][2] = 2
			self.droppingBlocks[self.totalcolumn//2][3] = 2
		elif self.blockType == 3:
			#  X
			# XXX
			self.droppingBlocks[self.totalcolumn//2][0] = 3
			self.droppingBlocks[self.totalcolumn//2-1][1] = 3
			self.droppingBlocks[self.totalcolumn//2][1] = 3
			self.droppingBlocks[self.totalcolumn//2+1][1] = 3
		elif self.blockType == 4:
			# X
			# XXX
			self.droppingBlocks[self.totalcolumn//2-1][0] = 4
			self.droppingBlocks[self.totalcolumn//2-1][1] = 4
			self.droppingBlocks[self.totalcolumn//2][1] = 4
			self.droppingBlocks[self.totalcolumn//2+1][1] = 4
		elif self.blockType == 5:
			#   X
			# XXX
			self.droppingBlocks[self.totalcolumn//2+1][0] = 5
			self.droppingBlocks[self.totalcolumn//2-1][1] = 5
			self.droppingBlocks[self.totalcolumn//2][1] = 5
			self.droppingBlocks[self.totalcolumn//2+1][1] = 5
		elif self.blockType == 6:
			# XX
			#  XX
			self.droppingBlocks[self.totalcolumn//2-1][0] = 6
			self.droppingBlocks[self.totalcolumn//2][0] = 6
			self.droppingBlocks[self.totalcolumn//2][1] = 6
			self.droppingBlocks[self.totalcolumn//2+1][1] = 6

	rotateCount = 0
	blockType = 0
	score = 0
	blockwidth = 30
	totalcolumn = 0
	totalrow = 0
	droppingBlocks = None
	settleBlocks = None
	purple_img = None
	green_img = None
	blue_img = None
	red_img = None
	orange_img = None
	yellow_img = None
	gameover = False

	def __init__(self,width,height):
		pygame.init()
		# clock = pygame.time.Clock()
		# clock.tick(1)

		self.totalrow = height//self.blockwidth
		self.totalcolumn = width//self.blockwidth

		self.purple_img = pygame.transform.scale(pygame.image.load("rc/purpleblock.png"),(self.blockwidth,self.blockwidth))
		self.green_img = pygame.transform.scale(pygame.image.load("rc/greenblock.png"),(self.blockwidth,self.blockwidth))
		self.blue_img = pygame.transform.scale(pygame.image.load("rc/blueblock.png"),(self.blockwidth,self.blockwidth))
		self.red_img = pygame.transform.scale(pygame.image.load("rc/redblock.png"),(self.blockwidth,self.blockwidth))
		self.orange_img = pygame.transform.scale(pygame.image.load("rc/orangeblock.png"),(self.blockwidth,self.blockwidth))
		self.yellow_img = pygame.transform.scale(pygame.image.load("rc/yellowblock.png"),(self.blockwidth,self.blockwidth))
	
	def init(self):
		gameover = False
		self.droppingBlocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		self.settleBlocks = [[0 for i in range(self.totalrow)] for j in range(self.totalcolumn)]
		self.addBlockIfNone()

tetris = Tetris(500,700)

pygame.display.set_caption("Tetris")
screen = pygame.display.set_mode((500,700))

font = pygame.font.Font(None,30)

gameover_img = pygame.transform.scale(pygame.image.load("rc/gameover.png"),(screen.get_width()/2,screen.get_height()/2))
background_img = pygame.transform.scale(pygame.image.load("rc/russia.png"),(screen.get_width(),screen.get_height()))

tetris.init()

# pygame.key.set_repeat(1)

clock = pygame.time.Clock()

while True:
	clock.tick(5)

	tetris.score += 1

	screen.blit(background_img,(0,0))
	tetris.drawGrid()
	if not tetris.gameover:
		tetris.dropBlock()
		tetris.addBlockIfNone()
		tetris.drawBlock(screen)
		tetris.cleanRow()
		tetris.drawScore(screen,font)
		if tetris.checkOverlap(tetris.droppingBlocks):
			tetris.gameover = True
	else:
		tetris.drawBlock(screen)
		tetris.drawScore(screen,font)
		screen.blit(gameover_img,
			((screen.get_width()-gameover_img.get_width())/2,
			(screen.get_height()-gameover_img.get_height())/2))

	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				tetris.leftBlock()
			elif event.key == pygame.K_RIGHT:
				tetris.rightBlock()
			elif event.key == pygame.K_UP:
				tetris.rotateBlock()	
		elif event.type == pygame.MOUSEBUTTONUP:
			if tetris.gameover:
				tetris.gameover = False
				tetris.init()
			else:
				tetris.fillFull()