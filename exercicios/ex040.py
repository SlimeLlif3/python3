n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1+n2)/2

print(f'Tirando {n1} e {n2}, a média do aluno é {média}')

if média <= 5.0:
    print('O aluno está REPROVADO.')

elif média > 5.0 and média < 6.9:
    print('O aluno está de RECUPERAÇÃO.')

else:
    print('O aluno está APROVADO.')
  

