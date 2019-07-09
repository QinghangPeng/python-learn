print('============== this is a first python exe ===============')
temp = input("你猜我现在心里想的数字是多少:")
guess = int(temp)
if guess == 6:
    print("66666666")
else:
    print("果然我们没有心灵感应")
print("this exe over")

# 引号中套用引号，可以单双引号复用
s = "Let's go!"
print(s)

# 当一个字符串中出现多个需要转义的字符时，可以在字符前面加上r
st = r"C:\programs\files\keke"
print(st)

# 对多行字符串快速换行 前后使用三个双引号 前提是换行的必须在定义字符串的时候
# 就换行，不能写一排
k = """窗前明月光,
疑是地上霜.
举头望明月,
低头思故乡."""
print(k)


