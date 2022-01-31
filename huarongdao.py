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

def drawBoard():
	for i in range(4):
		for j in range(4):
			screen.blit(block_img_map[board[j][i]],(j*100,i*100))

pygame.display.set_caption("华容道")
screen = pygame.display.set_mode((400,500))

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
		