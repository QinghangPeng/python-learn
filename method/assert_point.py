print("==== python 中的断言 assert ====")
# 当这个关键字后边的条件为false的时候，程序会自动崩溃，并抛出AssertionError
temp = int(input("请输入一个数字："))
assert temp > 5
print(temp)

# 作用为在程序中设置检查点
# 当需要确保程序中的某个条件一定为true才能让程序正常工作的时候，assert就可以发挥其作用
