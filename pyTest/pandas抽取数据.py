import pandas as pd

# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

data =[[110,125,99],[135,22,22],[111,22,33],[44,33,55]]
columns = ['语文', '数学', '英语']
index = ['我们','的恋爱','是对生命的','严重浪费']
df = pd.DataFrame(data=data, index=index, columns=columns)

# 抽取一行数据
print(df.loc['我们'])
print(df.iloc[0])

# 抽取多行数据
print(df.loc[['我们','的恋爱']])
print(df.iloc[[0,1]])

# 抽取连续任意多行数据
print(df.loc['我们':'严重浪费'])
print(df.iloc[0:3])


# 抽取指定列数据，可以直接使用列名，也可以使用loc属性和iloc属性
print(df['语文'])     # 直接使用列名
print(df.loc[:, ['语文']])
print(df.iloc[:, [0, 1]])
print(df.iloc[:, :2])

# 抽取一个数据，返回的是数字，不是DataFrame对象
print(df.loc['我们', '数学'])
print(df.iloc[0,1])

# 抽取指定行列数据
print(df.loc[['我们'], ['数学']])

# 按成绩条件抽取数据
print(df['语文']>105)
print(df.loc[df['语文'] > 105])
