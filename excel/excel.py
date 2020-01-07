import openpyxl

# 需要读取的文件
book_name_xls = '/home/stealhao/下载/公安部/公交站点、线路/ÏßÂ·ÐÅÏ¢±í20200106.xlsx'

sheet_name_xlsx = 'Sheet1'

# 需要写出的文件
product_name_xls = '/home/stealhao/下载/公安部/静态数据/公交/公交线路信息采集.xlsx'

# 读取excel
def read_excel_xlsx(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]
    b = []
    for row in sheet.rows:
        a = []
        for cell in row:
            if cell.column_letter  in ['C','F','G']:
                a.append(cell.value)
        b.append(a)
    write_excel_xlsx(product_name_xls,sheet_name_xlsx,b)

# 写入excel
def write_excel_xlsx(path, sheet_name, value):
    index = len(value)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
    workbook.save(path)
    print("xlsx格式表格写入数据成功！")


read_excel_xlsx(book_name_xls,sheet_name_xlsx)