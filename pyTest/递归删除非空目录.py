
import os

local_path = r'C:\Users\F1241948\Desktop\doe - por\test'

def list_files(local_path):
    """
    根据本地路径，返回路径下所有的文件和文件夹
    :param local_path:
    :return:
    """
    all_files = []
    if os.path.isdir(local_path):
        for file in os.listdir(local_path):
            filename = os.path.join(local_path, file)
            if os.path.isdir(filename):
                all_files.extend(list_files(filename))
            else:
                if os.path.exists(filename):
                    os.remove(filename)
        if os.path.exists(local_path):
            os.rmdir(local_path)
    else:
        if os.path.exists(local_path):
            os.remove(local_path)
    return all_files

list_files(local_path)