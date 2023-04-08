import csv
def writescv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='')as file:
        fw = csv.writer(file) #ตัวเขียนfile writter
        fw.writerow(datalsit) #ตัวtable datalist = ['pen','ensil','ersser']

def readscv():
    with open('data.csv',encoding='utf-8',newline='')as file:
        fr = csv.reader(file) #ตัวเขียนfile reader
        data = list(fr)
    return data



data = readscv()
print(data)

#data = ['ขนมเยลลี่',20,'7:29น.']
#writescv(data)
