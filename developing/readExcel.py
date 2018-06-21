import xlrd

def read_excel():
    workbook=xlrd.open_workbook('双色球统计结果.xls')
    print(workbook.sheet_names())
    sheet=workbook.sheet_by_name('sheet1')
    print(('this sheet has %d rows,%d cols')%(sheet.nrows,sheet.ncols))
    for i in range(sheet.nrows):
        list_row=[]
        for j in range(sheet.ncols):
            list_row.append(sheet.cell(i,j))
        print(list_row)
import pandas as pd
def pandas_read_excel():
    excel_path='双色球统计结果.xls'
    d=pd.read_excel(excel_path )
    print(d)
if __name__=='__main__':
    #read_excel()
    pandas_read_excel()