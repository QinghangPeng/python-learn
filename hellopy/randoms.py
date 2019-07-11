import random
secret = random.randint(1, 10)
print("============= 随便乱猜游戏 ===============")
temp = input("你猜我现在心里想的数字是多少：")
guess = int(temp)
while guess != secret:
    temp = input("猜错了，请重新输入：")
    guess = int(temp)
    if guess == secret:
        print("恭喜你，猜对了")
    else:
        if guess > secret:
            print("大了，大兄弟")
        else:
            print("小了，小老弟")
print("游戏结束，无聊的一匹")
