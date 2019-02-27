import os

BASE_PATH = r'F:\浙大日语\TEMP'
for root, dirs, files in os.walk(BASE_PATH):
    print(files)  #当前路径下所有非目录子文件
