print("==== python 中的 for 循环 以及配合range()的使用 ====")
temp = str(input("请输入一句话:"))
for i in temp:
    print(i, end=' ')

print("\n")
members = ['这是一个测试', '你好', 'hello', 'world']
for each in members:
    print(each, len(each))
    print(each, len(members))

print("\n")
for each in members:
    print(each, len(members))

# 可以看出 len指的是长度  each指的打印每个成员的长度  members指的打印数组的长度

print("\n")
# range(start,end,step) 三个参数，start和step都是非必填的
# 代表的是从start出发 每次递增step 到end结束

# java中 for(i=0;i<9;i++) ==> for i in range(9)
for i in range(9):
    print(i)

print("\n")
for i in range(2, 9):
    print(i)

print("\n")
for i in range(1, 10, 2):
    print(i)

# 将range产生的数装入list中
print(list(range(9)))
