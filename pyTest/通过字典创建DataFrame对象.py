import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

# 数据是字典，一个键值对就是一列的数据
df = pd.DataFrame({
    '语文': [110, 105, 95],
    '数学': [102, 150, 149],
    '英语': [83, 75, 99],
    '班级': '高一一班'
}, index=[0, 1, 2])

# 值时单个数据是，每一行都添加了相同的数据高一一班3

print(df)

