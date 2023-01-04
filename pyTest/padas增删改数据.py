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
df.loc['小口天'] = [12,23,45,56,78,89]
print(df)
# 增加多行数据
df_insert = pd.DataFrame({'语文':[100,123,138], '数学':[100,123,138], '英语':[100,123,138], '物理':[100,123,138], '化学':[100,123,138], '生物':[100,123,138]}, index=['刘辉','刘磊','李吉辉'])
df = pd.concat([df, df_insert])
print(df)

# 修改行、列标题
# 修改一个列名
df.columns = ['语文','生物','数学（上）', '英语', '物理', '化学']  # 即使只修改一个，也要将所有的列标题写上，否则会报错
print(df)
# 修改多个列名
df.rename(columns={'语文':'语文（上）', '数学（上）': '数学'}, inplace=True)      # replace为True表示直接修改df，否则不修改df，只返回修改后的数据
print(df)
# 修改行标签
df.index = list('12345678')
print(df)
df.rename({'1':11,'2':'22'}, axis=0, inplace=True)
print(df)

# 修改数据
# 修改整行数据
df.loc[11] = [11,12,12,12,12,21]
print(df)
df.loc[11] = df.loc[11] + 100
print(df)
df.iloc[0,:]=[11,11,11,11,11,11]
print(df)
# 修改整列数据
df.loc[:, '生物'] = [111,111,111,111,11,111,111,111]
print(df)
df.iloc[:, 0] = [111,111,111,111,11,111,111,111]
print(df)
# 修改某一处数据
df.loc[11, '生物'] = 201
print(df)
df.iloc[0,0] =100
print(df)

# 删除数据
# 删除行列数据
df.drop(['数学'], axis=1, inplace=True)       # 删除某一列
print(df)
df.drop([11, '22',], inplace=True)          # 删除某一行
print(df)
df.drop(['3'], axis=0, inplace=True)   # 删除一行
print(df)
df.drop(columns='生物', inplace=True)     # 删除columns为生物的列
print(df)
df.drop(labels='英语', axis=1, inplace=True)      # 删除列标签为英语的列
print(df)
df.drop(index='4', inplace=True)        # 删除index为'4'的行
df.drop(labels='5', axis=0, inplace=True)       # 删除行标签为'5'的行
print(df)
# 删除特定条件的行
print(df['物理'].isin([100]).index[1])        # 删除特定数据不会啊


