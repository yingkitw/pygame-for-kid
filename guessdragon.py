import random

def 卖广告():
	print("我是一条神龙，我住在哪个洞里啊？你猜猜，1还是2?")

def 写答案():
	return random.randint(1,2)

def 要答案():
	return input("山洞 1 还是 山洞 2:")

def 看看对不对(你的答案, 标准答案):
	if int(你的答案) == int(标准答案):
		print("大神")
	else:
		print("菜鸟")
#######################

卖广告()

答案 = 写答案()

# print(答案)

cave = 要答案()

# print('cave'+cave)

看看对不对(cave,答案)
cave = 要答案()

看看对不对(cave,答案)