print("==== python 中的break、continue 语句 ====")
temp = int(input("请输入我现在想的数字:"))
while True:
    if temp == 8:
        break
    temp = int(input("猜错了，请重新输入（只有猜到才能推出有游戏）："))
print("我们真是有心灵感应")

# continue语句
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
