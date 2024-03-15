soma = 0
hVelho = 0
mulher = 0
for c in range(1,5):
    print('------ {} PESSOA ------ '.format(c))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if sexo == 'M':
        if idade > hVelho:
            hVelho = idade
            nomeH = nome
    if sexo == 'F':
        if idade < 20:
            mulher += 1
print('A média de idade do grupo é de {} anos'.format((soma/4)))
print('O homem mais velho tem {} anos e se chama {}.'.format(hVelho, nomeH))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))