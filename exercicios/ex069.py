maior = homem = mulher = 0
while True:
    print('--' * 15)
    print('      CADASTRE UMA PESSOA')
    print('--' * 15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('--' * 15)
    while sexo != 'M' and sexo != 'F':
        print('Opção inválida, digite uma das opções disponiveis por favor.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continua != 'S' and continua != 'N':
        print('Opção inválida, digite [S/N] ')
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1 
    if continua == 'N':
        print(f'Total de pessoas com mais de 18 anos: {maior}')
        if homem == 1:
            print(f'Ao todo temos {homem} homem cadastrado')
        else: 
            print(f'Ao todo temos {homem} homens cadastrados')
        if mulher == 1:
            print(f'E temos {mulher} mulher com menos de 20 anos')
        else:
            print(f'E temos {mulher} mulheres com menos de 20 anos')
        break

        





