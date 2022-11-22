

def com_csv(old_file, new_file):
    """
    比较两个csv文件是否一致
    :param old_file:第一个文件路径
    :param new_file:第二个文件路径
    :return:返回结果true or false
    """
    if old_file.endswith(".csv") and new_file.endswith(".csv"):
        import csv
        old_result = []
        new_result = []
        with open(old_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for i in spamreader:
                old_result.append(i)

        with open(new_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for i in spamreader:
                new_result.append(i)

        print(old_result == new_result)



def com_excel(old_file, new_file):
    """比较两个excel是否一致"""
    if old_file.endswith(".xlsx") and new_file.endswith(".xlsx"):
        import xlrd
        old_excel = xlrd.open_workbook(old_file)
        new_excel = xlrd.open_workbook(new_file)

        old_result = []
        new_result = []

        # 获取所有sheet名称
        for table in old_excel.sheet_names():
            old_result.append(old_excel.sheet_by_name(table)._cell_values)

        for table in new_excel.sheet_names():
            new_result.append(new_excel.sheet_by_name(table)._cell_values)

        print(old_result == new_result)



if __name__ == '__main__':

    old_file = r"C:\Users\F1241948\Desktop\OTA測試數據\select item\old\resultcsv\ROW2_old.csv"
    new_file = r"C:\Users\F1241948\Desktop\OTA測試數據\select item\new\resultcsv\ROW2.csv"

    com_csv(old_file, new_file)
    com_excel(old_file, new_file)


