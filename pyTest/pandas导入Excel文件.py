import pandas as pd

# 解决数据输出时列名不对齐问题
pd.set_option('display.unicode.east_asian_width', True)


# 正常导入
df = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test2.xlsx')
print(df)

# 导入指定sheet页的数据
df2 = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test.xlsx', sheet_name='Limit')    # 指定sheetname
print(df2)

# 指定行索引导入Excel数据
df3 = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test2.xlsx', index_col=2)
print(df3)

# 指定列索引导入Excel数据
df4 = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test2.xlsx', header=3)
print(df4)

# 将数字作为列索引，通过设置header=None
df5 = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test2.xlsx', header=None)
print(df5[5])

# 导入指定列，例如导入第一列和第四列
df6 = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test2.xlsx', usecols=[0, 5])    # 也可以通过指定列名导入
print(df6)

