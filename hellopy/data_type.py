print("========== 两个用于判断数据类型的函数 =========")

# 获取当前值的数据类型
a = type(520)
print(a)

# 第一个参数代表需要判断的值  第二个参数代表期望该参数的类型  返回true 和 false
b = isinstance(520, str)
print(b)
