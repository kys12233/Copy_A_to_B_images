#根据txt文件生成文件夹。
import os
open_txt_path = 'test02_set_path.txt'

with open(open_txt_path, "r") as file:
    f = file.readlines()
    file.close()

for i in range(len(f)):
    f[i] = f[i].split('\n')[0]

for i in range(len(f)):
    os.makedirs(f[i])

