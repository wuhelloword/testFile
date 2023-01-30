import os
import time

path = r'C:\Users\F1241948\Desktop\D37 test log for tool use'


start = time.time()
file_data = []
for dirs in os.listdir(path):        # 最外层

    ce_path = os.path.join(os.path.join(path, dirs), 'CE')
    re_path = os.path.join(os.path.join(path, dirs), 'RE')
    ce_re_list = []
    if os.path.exists(ce_path):
        ce_re_list.append(ce_path)
    if os.path.exists(re_path):
        ce_re_list.append(re_path)

    for ce_re_dir in ce_re_list:

        for dir in os.listdir(ce_re_dir):
            print(dir)
            if 'FXGL' in dir:
                dir_path = os.path.join(ce_re_dir, dir)
                for file in os.listdir(dir_path):
                    file_path = os.path.join(dir_path,file)
                    if os.path.isfile(file_path) and file_path.endswith('.txt'):
                        with open(file_path, 'r') as f:
                            print(file_path)
                            data = f.readline()
                            file_data.append(data)

# print(file_data)
end = time.time()
print(end-start)
