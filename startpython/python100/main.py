# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


list1=[1,24,34,44,533,5,219]
for i in enumerate(list1):#按索引
    print(i)


list1=[1,24,34,44,533,5,219]
for i in range(len(list1)):#通过下标
    print(list1[i])

my_list = [1,2,2,3,3,3,4,4,4,4,5]
you_list = [i*2 for i in my_list]
print(you_list)
