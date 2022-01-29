import random

print("你好，这是一个猜数字的游戏，你猜猜1到20的数字")
answer = random.randint(1,20)
# print("my answer is  "+str(answer))

for i in range(10):
	guess = int(input())
	print("你第"+str(i)+"次猜的答案是"+str(guess))
	if guess == answer:
		print("你赢了")
		break
	elif guess > answer:
		print("太大了，再来一次")
	elif guess < answer:
		print("太小了，再来一次")
	else:
		print("loser, try again")

print("真正的答案是"+str(answer))	
# qwer = input()
# print("your answer is  "+qwer)