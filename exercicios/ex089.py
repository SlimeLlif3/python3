lista = []
dados = []
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    lista.append(dados[:])
    dados.clear()
    continua = str(input('Quer continuar? [S/N]')).strip().upper()
    while continua not in 'SN':
        print('Opção inválida! Por favor digite [S/N]')
        continua = str(input('Quer continuar? [S/N]')).strip().upper()
    if continua in 'N':
        print('-=' * 50)
        print('No. NOME           MÉDIA')
        print('-' * 40)
        for c,v in enumerate(lista):
            print(f'{c}   {lista[c][0]}            {(lista[c][1] + lista[c][2]) / 2}')
        print('-=' * 40)
        while True:
            aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            while aluno > c and aluno != 999:
                print('Esse aluno não existe! Digite um número de acordo com os alunos acima.')
                aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
            if aluno == 999:
                break
            print(f'Notas de {lista[aluno][0]} são [{lista[aluno][1]}, {lista[aluno][2]}]')
            print('-=' * 40)
        break
            
        

    



    