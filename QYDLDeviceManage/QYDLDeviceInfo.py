from mailmerge import MailMerge
import xlrd
import time
import os

'''
读取excel数据
'''
def readExcel():
    fileNameDate = '主机设备信息清单-硬件状态巡检.xlsx'
    filePathDate = os.path.join(os.getcwd(), fileNameDate)
    print(filePathDate)
    wb = xlrd.open_workbook(filePathDate)
    sheet1 = wb.sheet_by_name('资料收集')

    templateName='设备台账模板（主机设备）.docx'
    filePath=os.path.join(os.getcwd(),templateName)
    #打印模板路径
    print(filePath)
    #创建邮件合并文档并查看所有字段




    rowNum=sheet1.nrows

    for num in range(2,rowNum):
        document_1 = MailMerge(filePath)
        print("Fileds include in {}:{}".format(filePath, document_1.get_merge_fields()))
        dataCol = sheet1.row_values(num, 0, 12)
        print(dataCol)
        # 填充模板
        document_1.merge(
        Model=dataCol[4]+dataCol[5],
        OSVersion=dataCol[11],
        dateManufacture=u'待补充',
        serialNumber=str(dataCol[6]),
        Location=dataCol[0],
        Contract=u'待补充',
        deviceName=dataCol[3],
        IPAddress=dataCol[7],
        Service=dataCol[3],
        CPUinfo=dataCol[8],
        Memory=dataCol[9],
        Harddisk=dataCol[10],
        )
        print(document_1)
        if dataCol[4]+dataCol[5]!='':
            fileName = "DeviceInfo\\" + dataCol[0] + dataCol[3] + '.docx'
            document_1.write(os.path.join(os.getcwd(), fileName))
        document_1.close()



    #print(dataCol[0])
    #return dataCol


'''
写入doc模板
'''
def writeDocx():
    pass


'''
生产台账文档
'''
def productionDoc():
    pass


if __name__=="__main__":
    #productionDoc()
    readExcel()