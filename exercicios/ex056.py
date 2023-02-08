cont = 0
maioridade = 0
name = ''
mulher = 0
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    cont += idade
    total = (cont/2)/2

    if sexo == 'M':
        if p == 1:
            maioridade = idade
            name = nome
        elif maioridade < idade:
            maioridade = idade
            name = nome
    if sexo == 'F' and idade < 20:
        mulher += 1

print(f'A média de idade do grupo é de {total} anos')
print(f'O homem mais velho tem {maioridade} anos e se chama {name}.')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos.')

    



  
