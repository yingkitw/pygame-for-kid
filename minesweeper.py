import sys, pygame, random

class MineSweeper:

	total_column = 0
	total_row = 0

	flagMode = False

	gameover = False

	mark = []
	mine = []
	answer = []
	hint = []

	def checkWin(self):
		for i in range(self.total_column):
			for j in range(self.total_row):
				if self.mark[i][j] != self.answer[i][j]:
					return False
				elif self.mine[i][j] == 0 and self.answer[i][j] == 0:
					return False
		return True

	def checkGameover(self):
		for i in range(self.total_column):
			for j in range(self.total_row):
				if self.mine[i][j] == 1 and self.mine[i][j] == self.answer[i][j]:
					return True
		return False

	def uncover_empty(self,i,j):
		if i < 0 or i >= self.total_column:
			return False
		elif j < 0 or j >= self.total_row:
			return False
		elif self.answer[i][j] == 0 and self.mine[i][j] == 0:
			self.mine[i][j] = 1
			return True
		else:
			return False

	def uncover(self):
		for i in range(self.total_column):
			for j in range(self.total_row):
				if self.mine[i][j] == 1 and self.answer[i][j] == 0:
					found = self.uncover_empty(i-1,j) \
					and self.uncover_empty(i,j-1) \
					and self.uncover_empty(i,j+1) \
					and self.uncover_empty(i+1,j)
					if found:
						self.uncover()

	def printMark(self):
		print(self.mark)

	def get_bomb(self,i,j):
		if i < 0 or i >= self.total_column:
			return 0
		elif j < 0 or j >= self.total_row:
			return 0
		else:
			return self.answer[i][j]

	def get_surrounding(self,i,j):
		total = 0
		total += self.get_bomb(i-1,j-1)
		total += self.get_bomb(i-1,j)
		total += self.get_bomb(i-1,j+1)
		total += self.get_bomb(i,j-1)
		total += self.get_bomb(i,j+1)
		total += self.get_bomb(i+1,j-1)
		total += self.get_bomb(i+1,j)
		total += self.get_bomb(i+1,j+1)
		return total

	def init(self):
		self.gameover = False
		self.mark = [[0 for i in range(self.total_row)] for j in range(self.total_column)]
		self.mine = [[0 for i in range(self.total_row)] for j in range(self.total_column)]
		self.answer = [[random.randint(0,8) >= 7 for i in range(self.total_row)] for j in range(self.total_column)]
		self.hint = [[0 for i in range(self.total_row)] for j in range(self.total_column)]
		for i in range(self.total_column):
			for j in range(self.total_row):
				self.hint[i][j] = self.get_surrounding(i,j)

	def scale_block(self,img):
		return pygame.transform.scale(img,(self.cell_width,self.cell_height))

	def drawCell(self, img, c,r):
		screen.blit(img,(c*self.cell_width,r*self.cell_height),(0,0,self.cell_width,self.cell_height))

	def drawGameover(self):
		for c in range(self.total_column):
			for r in range(self.total_row):
				if self.mine[c][r] == 1 and self.answer[c][r] == 1:
					self.drawCell(bomb_red_img,c,r)
				elif self.mark[c][r] == 1 and self.answer[c][r] == 1:
					self.drawCell(flag_img,c,r)
				elif self.answer[c][r] == 1:
					self.drawCell(bomb_img,c,r)
				elif self.hint[c][r] >= 1 and self.hint[c][r] <= 8:
					self.drawCell(hint_img_map[self.hint[c][r]],c,r)
				else:
					self.drawCell(empty_img,c,r)

	def drawBoard(self):
		for c in range(self.total_column):
			for r in range(self.total_row):
				if self.mark[c][r] == 1:
					self.drawCell(flag_img,c,r)
				elif self.mine[c][r] == 1 and self.answer[c][r] == 0:
					if self.hint[c][r] >= 1 and self.hint[c][r] <= 8:
						self.drawCell(hint_img_map[self.hint[c][r]],c,r)
					else:
						self.drawCell(empty_img,c,r)
				elif self.mark[c][r] == 0:
					self.drawCell(block_img,c,r)

	def get_cell(self,x,y):
		column = int(x // self.cell_width)
		row = int(y // self.cell_height)
		return column, row
pygame.init()

screen = pygame.display.set_mode((700,500))
x, y = screen.get_width(),screen.get_height()
ms = MineSweeper()
ms.total_column = 14
ms.total_row = 10
ms.cell_width = x/ms.total_column
ms.cell_height = y/ms.total_row
ms.init()

pygame.display.set_caption("扫雷")

block_img = ms.scale_block(pygame.image.load("block.png"))
empty_img = ms.scale_block(pygame.image.load("empty.png"))
bomb_img = ms.scale_block(pygame.image.load("bomb.png"))
bomb_red_img = ms.scale_block(pygame.image.load("bomb red.png"))
bomb_wrong_img = ms.scale_block(pygame.image.load("bomb wrong.png"))
flag_img = ms.scale_block(pygame.image.load("flag.png"))
mark1_img = ms.scale_block(pygame.image.load("mark1.png"))
mark2_img = ms.scale_block(pygame.image.load("mark2.png"))
mark3_img = ms.scale_block(pygame.image.load("mark3.png"))
mark4_img = ms.scale_block(pygame.image.load("mark4.png"))
mark5_img = ms.scale_block(pygame.image.load("mark5.png"))
mark6_img = ms.scale_block(pygame.image.load("mark6.png"))
mark7_img = ms.scale_block(pygame.image.load("mark7.png"))
mark8_img = ms.scale_block(pygame.image.load("mark8.png"))
win_img = pygame.transform.scale(pygame.image.load("win.png"),(screen.get_width()/2,screen.get_height()/2))
gameover_img = pygame.transform.scale(pygame.image.load("gameover.png"),(screen.get_width()/2,screen.get_height()/2))
hint_img_map = {1:mark1_img,2:mark2_img,3:mark3_img,4:mark4_img,5:mark5_img,6:mark6_img,7:mark7_img,8:mark8_img}

while True:
	screen.fill((255,255,255))
	ms.uncover()
	if ms.checkWin():
		ms.drawBoard()
		screen.blit(win_img,
		((screen.get_width()-win_img.get_width())/2,
		(screen.get_height()-win_img.get_height())/2))
	elif ms.checkGameover():
		ms.gameover = True
		ms.drawGameover()
		screen.blit(gameover_img,
		((screen.get_width()-win_img.get_width())/2,
		(screen.get_height()-win_img.get_height())/2))
	else:
		ms.drawBoard()
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			if ms.gameover:
				ms.init()
			else:
				x, y = pygame.mouse.get_pos()
				column,row = ms.get_cell(x,y)
				key = pygame.key.get_pressed()
				if ms.flagMode:
					if ms.mark[column][row] == 1:
						ms.mark[column][row] = 0
					else:
						ms.mark[column][row] = 1
				else:
					ms.mine[column][row] = 1
		elif event.type == pygame.KEYDOWN \
			and event.key == pygame.K_LSHIFT:
			ms.flagMode = True
		elif event.type == pygame.KEYUP \
			and event.key == pygame.K_LSHIFT:
			ms.flagMode = False
			# printMark()