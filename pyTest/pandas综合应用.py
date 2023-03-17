import pandas as pd
import glob

# 1. Excel多表合并
filearray = []
# 指定目录下的所有Excel文件
filelocation = glob.glob(r'C:\Users\F1241948\Desktop\joyful-pandas-master\data\*.xlsx')
# 遍历指定目录
for filename in filelocation:
    filearray.append(filename)
    print(filename)
res = pd.read_excel(filearray[0])
print(res)

# 顺序读取Excel文件进行合并
for i in range(1, len(filearray)):
    A = pd.read_excel(filearray[i])
    res = pd.concat([res, A], ignore_index=True, sort=False)

# 写入Excel文件并保存
writer = pd.ExcelWriter('test.xlsx')
res.to_excel(writer, 'sheet1')
writer.save()

