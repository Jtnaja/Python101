def  writedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('kuy world')
def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        file.writelines(text+ '\n')


def readdata():
    with open('add-data.txt',encoding='utf-8') as file:
        data = file.readlines()
        print(data)



readdata()






        
#adddata('ดินสอ10บาท')
#adddata('ไมค์10บาท')
#adddata('เมาส๋10บาท')
