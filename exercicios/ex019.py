from random import choice
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input(' Terceiro nome; ')
n4 = input('Quarto nome: ')
ale = [n1, n2, n3, n4]
escolha = choice(ale)

print('O aluno escolhido foi {}'.format(escolha))