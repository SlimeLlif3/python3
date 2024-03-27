lista = []
for c in range (5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        print('Adicionado ao final da lista...')
        lista.insert(4,valor)
    if valor < lista[0]:
        print('Adicionado na posição 0')
        lista.insert(0,valor)
    if valor > lista [0] and valor < lista [1]: 
        print('Adicionado na posição 1')
        lista.insert(1,valor)   
print(lista)
