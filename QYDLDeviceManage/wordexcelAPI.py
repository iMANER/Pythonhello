import xlrd
import time
import os
from  datetime import date,datetime

def readExcel():
    a=time.perf_counter()
    #f=xlrd.open_workbook('G:/PycharmProjects/Pythonhello/日常巡检记录表/主机设备信息清单-硬件状态巡检.xlsx')

    fileName='主机设备信息清单-硬件状态巡检.xlsx'
    filePath=os.path.join(os.getcwd(),fileName)
    print(filePath)
    f=xlrd.open_workbook(filePath)

    sheet1 = f.sheet_by_name('资料收集')
    print(sheet1.cell(10,3).value)
    b=time.perf_counter()
    print('读取时间:',b-a)
    print(f.sheet_names())
    print(f.nsheets)
    print(f.sheets())
    print(f.sheet_by_index(0))
    #获取sheet的汇总数据
    print('---------------获取sheet的汇总数据------------------')
    print(sheet1.name)
    print(sheet1.nrows)
    print(sheet1.ncols)
    #单元格批量读取
    print("---------------单元格批量读取--------------------")
    print(sheet1.row_values(3))
    print(sheet1.row(3))
    print(sheet1.row_types(3))

    #表操作
    print(sheet1.row_values(0,6,10))#取第1行，第6~10列（不含第10表）
    print(sheet1.col_values(0,0,5))
    print(sheet1.row_slice(2,1,3))
    print(sheet1.row_types(1,0,3))

    #特定单元格读取
    #a)获取单元格值
    print(sheet1.cell(1,3))
    print(sheet1.cell(1,3).value)
    print(sheet1.row(1)[3].value)

    #b)获取单元格类型
    print(sheet1.cell(1,3).ctype)
    print(sheet1.cell_type(1,3))
    print(sheet1.row(1)[3].ctype)

    '''
    转换
    (0,0)转换成A1
    (0,0)转换成$A$1
    数字转换为字母AE
    '''
    print(xlrd.cellname(0,0))
    print(xlrd.cellnameabs(0,0))
    print(xlrd.colname(3))




from mailmerge import MailMerge
def writeDocx():
    templateName='设备台账模板（主机设备）.docx'
    filePath=os.path.join(os.getcwd(),templateName)
    #打印模板路径
    print(filePath)
    #创建邮件合并文档并查看所有字段
    document_1=MailMerge(filePath)
    print("Fileds include in {}:{}".format(filePath,document_1.get_merge_fields()))

    #填充模板
    document_1.merge(
        Model=u'勒布朗',
        OSVersion='123456789',
        dateManufacture='2018',
        serialNumber='7',
        Location=u'洛杉矶湖人',
        Contract=u'联盟第一人',
        deviceName=u'联盟第一人',
        IPAddress=u'联盟第一人',
        Service=u'联盟第一人',
    )
    fileName='123456.docx'
    document_1.write(os.path.join(os.getcwd(),fileName))



if __name__=="__main__":
    readExcel()
    #writeDocx()