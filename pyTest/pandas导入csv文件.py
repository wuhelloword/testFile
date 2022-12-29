
import pandas as pd

# 设置数据显示的最大列数和宽度
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# 解决数据输出时列名不对齐问题
pd.set_option('display.unicode.east_asian_width', True)

# 导入csv文件，并指定编码格式
df = pd.read_csv(r'C:\Users\F1241948\Desktop\joyful-pandas-master\data\audit.csv')
print(df)
