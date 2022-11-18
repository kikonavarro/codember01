'''import pandas

data = pandas.read_csv("users.txt")
list_users = []

for line in data:
    list_users.append(line)

print(list_users)'''

'''def is_in_array(list, buscar):
    for i in buscar:'''


with open('users.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    data2 = data.split('  ')

keys_mandatory = ['usr', 'eme', 'psw', 'age', 'loc', 'fll']
number = 0
number_correct = 0
for element in data2:
    element_split = element.split(' ')
    dict = {}

    for e in element_split:
        par = e.split(':')
        dict[par[0]] = par[1]

    keys_in_dict = []
    for key in dict:
        keys_in_dict.append(key)

    check = all(item in keys_in_dict for item in keys_mandatory)
    if check:
        print(f'{keys_in_dict}is correct')
        number_correct += 1
    else:
        print(f'{keys_in_dict}not correct')
        number += 1

len = len(data2)
print(len)
print(number)
print(number_correct)












'''usuario = ['email:kikonm']
usuario2 = usuario[0].split(':')

dicccionario = {}

dicccionario[usuario2[0]] = usuario2[1]

print(dicccionario)
'''





'''
usr: nombre de usuario
eme: email
psw: contraseña
age: edad
loc: ubicación
fll: número de seguidores
'''
