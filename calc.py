import random

print("剪刀石头布")

weapon = [2,0,5]

for i in range(305):
	hand = input("你出什么?剪刀[2],石头[0],布[5]")

	yourhand = weapon[random.randint(0,2)]

	if yourhand == 0:
		print("电脑出石头")
	elif yourhand == 2:
		print("电脑出剪刀")
	elif yourhand == 5:
		print("电脑出布")
	
	if int(hand) == yourhand:
		print("和，再来一局")
	elif (int(hand) == 2 and yourhand == 0)\
	or (int(hand) == 0 and yourhand == 5)\
	or (int(hand) == 5 and yourhand == 2):
		print("电脑赢")
	elif (int(hand) == 2 and yourhand == 5)\
	or (int(hand) == 0 and yourhand == 2)\
	or (int(hand) == 5 and yourhand == 0):
		print("我赢")
