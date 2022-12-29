


if __name__ == '__main__':
    pass
"""
# 生成器是特殊的迭代器
# 两种方法生成生成器：
# 1. 原来的列表推导式中的中括号变成小括号
    list1 = [i*2 for i in range(10)]
    print(list1)
    list2 = (i*2 for i in range(10))
    for i in list2:
        print(i)
        """
# 2. 定义一个函数，函数中有yeild，这个函数自动变成生成器
def create_num(all_num):
    a = 0
    b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        current_num += 1
        # print(a)
        yield a         # 如果一个函数中有yield语句，name这个就不再是函数，而是一个生成器的模板
        a, b = b, a+b
obj = create_num(10)      # 再调用create_num的时候，发现这个函数中yield，那么不是在调用函数，而是创建一个生成器对象

for i in obj:
    print(i)

