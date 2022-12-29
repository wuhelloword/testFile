import pandas as pd

# 解决数据输出时列名不对齐问题
pd.set_option('display.unicode.east_asian_width', True)

data =[[110,125,99],[135,22,22],[111,22,33],[44,33,55]]
columns = ['语文', '数学', '英语']
index = ['黄猛','冯光豪','方墉','张波']
df = pd.DataFrame(data=data, index=index, columns=columns)

# 按列增加数据：
# 直接为DataFrame对象赋值
df['物理'] = [88,78,70,98]
print(df)
# 使用loc属性在DataFrame对象的最后增加一列
df.loc[:,'化学'] = [99,96,99,99]
print(df)
# 在指定位置插入一列
wl = [89,78,45,12]
df.insert(1, '生物', wl)
print(df)

# 按行增加数据：
# 增加一行数据，主要使用loc属性
df.loc['小口天']