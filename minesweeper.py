import sys, pygame, random

def checkWin():
	for i in range(total_row):
		for j in range(total_column):
			if mark[i][j] != answer[i][j]:
				return False
			elif mine[i][j] == 0 and answer[i][j] == 0:
				return False
	return True

def checkGameover():
	for i in range(total_row):
		for j in range(total_column):
			if mine[i][j] == 1 and mine[i][j] == answer[i][j]:
				return True
	return False

def uncover_empty(i,j):
	if i < 0 or i >= total_column:
		return False
	elif j < 0 or j >= total_row:
		return False
	elif answer[i][j] == 0 and mine[i][j] == 0:
		mine[i][j] = 1
		return True
	else:
		return False

def uncover():
	for i in range(total_row):
		for j in range(total_column):
			if mine[i][j] == 1 and answer[i][j] == 0:
				found = uncover_empty(i-1,j) \
				and uncover_empty(i,j-1) \
				and uncover_empty(i,j+1) \
				and uncover_empty(i+1,j)
				if found:
					uncover()

def printMark():
	print(mark)

def get_bomb(i,j):
	if i < 0 or i >= total_column:
		return 0
	elif j < 0 or j >= total_row:
		return 0
	else:
		return answer[i][j]

def get_surrounding(i,j):
	total = 0
	total += get_bomb(i-1,j-1)
	total += get_bomb(i-1,j)
	total += get_bomb(i-1,j+1)
	total += get_bomb(i,j-1)
	total += get_bomb(i,j+1)
	total += get_bomb(i+1,j-1)
	total += get_bomb(i+1,j)
	total += get_bomb(i+1,j+1)
	return total

pygame.init()

total_column = 8
total_row = 8

flagMode = False

screen = pygame.display.set_mode((400,400))
x, y = screen.get_width(),screen.get_height()
cell_width = x/total_column
cell_height = y/total_row

gameover = False

mark = []
mine = []
answer = []
hint = []

gameover = False
mark = [[0 for i in range(total_column)] for j in range(total_row)]
mine = [[0 for i in range(total_column)] for j in range(total_row)]
answer = [[random.randint(0,8) >= 7 for i in range(total_column)] for j in range(total_row)]
hint = [[0 for i in range(total_column)] for j in range(total_row)]
for i in range(total_row):
	for j in range(total_column):
		hint[i][j] = get_surrounding(i,j)

def scale_block(img):
	return pygame.transform.scale(img,(cell_width,cell_height))

pygame.display.set_caption("踩地雷")

block_img = scale_block(pygame.image.load("block.png"))
empty_img = scale_block(pygame.image.load("empty.png"))
bomb_img = scale_block(pygame.image.load("bomb.png"))
bomb_red_img = scale_block(pygame.image.load("bomb red.png"))
bomb_wrong_img = scale_block(pygame.image.load("bomb wrong.png"))
flag_img = scale_block(pygame.image.load("flag.png"))
mark1_img = scale_block(pygame.image.load("mark1.png"))
mark2_img = scale_block(pygame.image.load("mark2.png"))
mark3_img = scale_block(pygame.image.load("mark3.png"))
mark4_img = scale_block(pygame.image.load("mark4.png"))
mark5_img = scale_block(pygame.image.load("mark5.png"))
mark6_img = scale_block(pygame.image.load("mark6.png"))
mark7_img = scale_block(pygame.image.load("mark7.png"))
mark8_img = scale_block(pygame.image.load("mark8.png"))
win_img = pygame.transform.scale(pygame.image.load("win.png"),(screen.get_width()/2,screen.get_height()/2))
gameover_img = pygame.transform.scale(pygame.image.load("gameover.png"),(screen.get_width()/2,screen.get_height()/2))

def drawCell(img, c,r):
	screen.blit(img,(c*cell_width,r*cell_height),(0,0,cell_width,cell_height))

def drawGameover(column, row):
	for c in range(column):
		for r in range(row):
			if mine[c][r] == 1 and answer[c][r] == 1:
				drawCell(bomb_red_img,c,r)
			elif mark[c][r] == 1 and answer[c][r] == 1:
				drawCell(flag_img,c,r)
			elif answer[c][r] == 1:
				drawCell(bomb_img,c,r)
			elif hint[c][r] == 1:
				drawCell(mark1_img,c,r)
			elif hint[c][r] == 2:
				drawCell(mark2_img,c,r)
			elif hint[c][r] == 3:
				drawCell(mark3_img,c,r)
			elif hint[c][r] == 4:
				drawCell(mark4_img,c,r)
			elif hint[c][r] == 5:
				drawCell(mark5_img,c,r)
			elif hint[c][r] == 6:
				drawCell(mark6_img,c,r)
			elif hint[c][r] == 7:
				drawCell(mark7_img,c,r)
			elif hint[c][r] == 8:
				drawCell(mark8_img,c,r)
			else:
				drawCell(empty_img,c,r)

def drawBoard(column, row):
	for c in range(column):
		for r in range(row):
			if mark[c][r] == 1:
				drawCell(flag_img,c,r)
			elif mine[c][r] == 1 and answer[c][r] == 0:
				if hint[c][r] == 1:
					drawCell(mark1_img,c,r)
				elif hint[c][r] == 2:
					drawCell(mark2_img,c,r)
				elif hint[c][r] == 3:
					drawCell(mark3_img,c,r)
				elif hint[c][r] == 4:
					drawCell(mark4_img,c,r)
				elif hint[c][r] == 5:
					drawCell(mark5_img,c,r)
				elif hint[c][r] == 6:
					drawCell(mark6_img,c,r)
				elif hint[c][r] == 7:
					drawCell(mark7_img,c,r)
				elif hint[c][r] == 8:
					drawCell(mark8_img,c,r)
				else:
					drawCell(empty_img,c,r)
			elif mark[c][r] == 0:
				drawCell(block_img,c,r)

def get_cell(x,y):
	column = int(x // cell_width)
	row = int(y // cell_height)
	return column, row

while True:
	screen.fill((255,255,255))
	uncover()
	if checkWin():
		drawBoard(total_column,total_row)
		screen.blit(win_img,
		((screen.get_width()-win_img.get_width())/2,
		(screen.get_height()-win_img.get_height())/2))
	elif checkGameover():
		drawGameover(total_column,total_row)
		screen.blit(gameover_img,
		((screen.get_width()-win_img.get_width())/2,
		(screen.get_height()-win_img.get_height())/2))
	else:
		drawBoard(total_column,total_row)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			x, y = pygame.mouse.get_pos()
			column,row = get_cell(x,y)
			key = pygame.key.get_pressed()
			if flagMode:
				if mark[column][row] == 1:
					mark[column][row] = 0
				else:
					mark[column][row] = 1
			else:
				mine[column][row] = 1
		elif event.type == pygame.KEYDOWN \
			and event.key == pygame.K_LSHIFT:
			flagMode = True
		elif event.type == pygame.KEYUP \
			and event.key == pygame.K_LSHIFT:
			flagMode = False
			# printMark()