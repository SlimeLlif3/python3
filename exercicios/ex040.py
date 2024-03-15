n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2 

print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, round(media, 1)))
if media < 5:
    print('O aluno está REPROVADO')
elif media >= 7:
    print('O aluno está APROVADO')
elif media > 5 and media < 6.9:
    print('O aluno está de RECUPERAÇÃO')
    

