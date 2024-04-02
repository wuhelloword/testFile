import numpy as np
print("1. 创建简单的数组")
n1 = np.array([1,2,3])              # 整数的一维数组
n2 = np.array([0.1,0.2,0.3])        # 小数的一维数组
n3 = np.array([[1,2],[3,4]])        # 二维数组
print(n1)
print(n2)
print(n3)
print(type(n1))



print("2. 为数组指定数据类型")
data = [1.0,2,3]
# 创建浮点型数组
n1 = np.array(data, dtype=np.float_)
# 或者
n1 = np.array(data, dtype=float)
print(n1)
print(n1.dtype)
print(type(n1[0]))

print("3. 数组的复制")
n1 = np.array([1,2,3])  # 创建数组
n2 = np.array(n1, copy=True)  # 复制数组
n2[0] = 3
n2[2] = 1
print(n1)
print(n2)

print("4. 通过ndmin参数修改数组的维数")
nd1 = [1,2,3]
nd2 = np.array(nd1, ndmin=3)
print(nd2)

# 创建指定维度和数据类型未初始化的数组
n = np.empty([2,3], dtype=int)
print(n)    # 这里的数组元素为随机值，因为他们未被初始化

# 创建指定维度（以0填充）的数组
n = np.zeros(3)
print(n)        # 默认是float

# 创建指定维度（以1填充）的数组
n = np.ones(3)
print(n)

# 创建指定维度和类型的数组并以指定值填充
n = np.full((3,3),8)
print(n)

# 通过数值范围创建数组
n = np.arange(1,12,3)
print(n)

# 使用
