import pandas as pd

# 解决数输出时列明不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)

data = [[110,105,99],[60,80,100],[109,120,130]]
index = [0,1,2]
columns = ['语文','数学','英语']

# 创建DataFrame数据
df = pd.DataFrame(data=data,index=index,columns=columns)
# print(df)
# print("--------------------")
for col in df.columns:
    # print(col)
    print(df[col])
