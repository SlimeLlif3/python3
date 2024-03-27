dado = []
lista = []
peso_maior = peso_menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        print('Opção incorreta! Por favor digite [S/N]')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    for c, v in enumerate(lista):
        if c == 0:
            peso_maior = lista[c][1]
            peso_menor = lista[c][1]
        elif lista[c][1] > peso_maior:
            peso_maior = lista[:][c][1]
        elif lista[c][1] < peso_menor:
            peso_menor = lista[c][1]
    if continuar in 'N':
        break
    
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {peso_maior}Kg. Peso de',end=' ')     
for p in lista:
    if p[1] == peso_maior:
        print(f'[{p[0]}]',end=' ')
print(f'\nO menor peso foi {peso_menor}Kg. Peso de ')
for pl in lista:
    if p[1] == peso_menor:
        print(f'[{p[0]}]',end=' ')
        

        
        
    

