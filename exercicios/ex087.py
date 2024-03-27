matrix = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma_par = terceira_coluna = segunda_coluna = 0
for l in range (0,3):
    for c in range (0,3):
        matrix[l][c]= int(input(f'Digite um valor para {[l],[c]}'))
        terceira_coluna += matrix[l][2]     
print('-=' * 30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[  {matrix[l][c]}  ]',end='')
        if matrix[l][c] % 2 == 0:
            soma_par += matrix[l][c]
    print() 
print('-=' * 30)
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
print(f'O maior valor da segunda linha é {max(matrix[1])}')


