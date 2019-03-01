import xlrd
import os.path
class Readexcel(object):
    @classmethod
    def read(self,excelpath,sheetName='Sheet1'):
        book=xlrd.open_workbook(excelpath)
        sheet=book.sheet_by_name(sheetName)
        keys=sheet.row_values(0)
        rowNum=sheet.nrows #行
        colNum=sheet.ncols  #列
        if rowNum<=1:
            print('行数小于1行，出现错误')
        else:
            list1=[]
            for i in range(1,rowNum):
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(colNum):
                    sheet_data[keys[j]]=values[j]

                list1.append(sheet_data)
                print(sheet_data)
            return  list1
if __name__=="__main__":
    file = os.path.dirname(os.path.abspath('.')) + '/utils/Sheet1.xlsx'
    Readexcel.read(file)