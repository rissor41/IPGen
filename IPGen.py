import re
print ("IPGen - это скрипт. Он подставляет в последний октета значения 24 маски подсетей.\nСкрипт позволяет быстро получить нужный блок адресов для дальнейшего взаимодействия с ним.")
x = input("Введите ip-адрес без крайнего октета: ")
point_counter = x.count('.')
if re.findall('\d+.\d+.\d+.', x) and len(x) <= 12 and point_counter == 3:
    for i in range(256):
        print(x + repr(i))
else:
    print ("It incorrent format")