# 生成需要创建的目录的列表
import os

open_txt_path = 'test01_replace.txt'
save_txt_path = 'test02_set_path.txt'



with open(open_txt_path, 'r') as file:
    f = file.readlines()
    file.close()


list_01 = []
for i in range(len(f)):
    a = f[i].split("/")
    b = ""
    for j in range(0,len(a)-1):
        b = b +'/'
        b = b + a[j]
    print(b[1:])
    list_01.append(b[1:])

c = set(list_01)
print(c)
d = list(c)
print(d)
with open(save_txt_path, "w") as file:
    for i in range(len(d)):
        file.write(d[i]+"\n")
    file.close()
