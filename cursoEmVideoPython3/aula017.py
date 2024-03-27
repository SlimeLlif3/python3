valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3 , 4 ,7]
#Sendo escrito dessa forma cria uma cópia da lista sem mudar os dois valores
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')