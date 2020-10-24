"""猜数游戏"""
import random

counts = 0
answer = random.randint(1, 100)

while counts >=0:
    temp = input("请输入一个100以内的正整数： ")
    guess = int(temp)

    if guess == answer:
        counts = counts + 1
        print("猜中啦！")
        print("你猜了：" + str(counts) + "次")
        break
    else:
        if guess < answer:
            print("小了")
        else:
            print("大了")
        counts = counts + 1

print("游戏结束")
