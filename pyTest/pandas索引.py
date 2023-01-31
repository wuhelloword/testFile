import pandas as pd

# 利用索引实现自动的数据对齐功能
s1 = pd.Series([10,20,30], index=list('abc'))
s2 = pd.Series([2,3,4], index=list('bcd'))
print(s1+s2)        # 得到的结果是abcd，值为NaN,22,33,NaN，自动对齐后bc对齐了，a和d的值加NaN还是NaN

# 重新设置Series对象索引
s3 = pd.Series([88,50,98], index=[1,2,3])
print(s3)
print(s3.reindex([1,2,3,4,5]))
# reindex向前和向后填充数据
print(s3.reindex([1,2,3,4,5,6], method='ffill'))
print(s3.reindex([1,2,3,4,5,6], method='bfill'))

# 对DataFrame对象重新设置索引
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
data = [[110,105,99],[105,88,101],[109,120,130]]
index=['mr001','mr003','mr005']
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
# 通过reindex方法重新设置行索引
df = df.reindex(['mr001','mr002','mr003','mr005','mr004'])
print(df)
# 通过reindex方法重新设置列索引
df = df.reindex(columns=['语文', '物理', '英语'])
print(df)   # 原来的列是语文数学英语，这样修改不是把数学的名称改为物理，而是没有数学这一列，多了物理这一列，且物理的值为NaN了
df = df.reindex(columns=['语文', '物理', '数学', '英语'])
print(df)
print('=========================')
# 通过reindex方法重新设置行索引和列索引
df = df.reindex(index=['mr001','mr002','mr003','mr004', 'mr006'], columns=['语文', '物理', '英语'])
print(df)

# 设置某列为索引
df = pd.read_excel(r'C:\Users\F1241948\Desktop\test\test2.xlsx')
print(df)       # 此时默认行索引为诶01234这种
# 修改第一列的数据作为行索引：
df = df.set_index(['列1'])
print(df)
df = df.set_index(['列2'], drop=False)       # drop默认是True，False的时候，这一列作为行索引的同时，数据中还有这一列数据
print(df)

# 数据清洗后重新设置连续的行索引
df = df.dropna().reset_index(drop=True)
