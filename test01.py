open_txt_path = 'test01.txt'
save_txt_path = 'test01_replace.txt'


with open(open_txt_path, 'r')as file:
    f = file.readlines()
    file.close()

replace_path = "F:/AI/Python/My_za/Copy_A_to_B_images"

list_01= []
for i in range(len(f)):
    print(f[i])
    a = f[i].split("/labeled")[0]
    b = f[i].replace(a, replace_path)
    list_01.append(b)


with open(save_txt_path, 'w') as file:
    for i in range(len(list_01)):
        file.write(list_01[i])
    file.close()

