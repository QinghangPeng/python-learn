print("==== 判断分数等级 方法一 ====")
score = int(input("请输入你的分数："))
if 90 <= score <= 100:
    print("A")
if 80 <= score < 90:
    print("B")
if 60 <= score < 80:
    print("C")
if 0 <= score < 60:
    print("D")
if score < 0 or score > 100:
    print("输入错误！")

# 这种写法会非常的耗费CPU 因为会执行每一个if条件，
# 与method2 method3相比较而言  不推荐这种写法
