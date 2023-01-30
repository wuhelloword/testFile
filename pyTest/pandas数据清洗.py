import pandas as pd

df =pd.read_excel(r'C:\Users\F1241948\Desktop\joyful-pandas-master\data\color.xlsx')

# 查看缺失值
print(df)
print(df.info())
print(df.isnull())
print(df.notnull())

# 删除缺失值
df.drop()
df.dropna(how='all')
df1 = df[df['X1'].notnull()]
print(df1)

# 填充缺失值
df['X1'] = df['X1'].fillna(0)     # 填充X1列空值为0


# 重复值处理
# 判断每一行数据是否重复（完全相同）
print(df.duplicated())      # 如果返回值为False，表示不重复；返回值为True,表示重复。
# 去除全部的重复数据
df.drop_duplicates()
# 去除指定列的重复数据
df.drop_duplicates(['X1'])
# 保留重复行中的最后一行
df.drop_duplicates(['X1'], keep='last')
# 直接删除，保留一个副本
df.drop_duplicates(inplace=False)
# inplace=True表示直接在原来的DataFrame对象上删除重复项，而默认值False表示删除重复项后再生成一个副本

