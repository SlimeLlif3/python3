from random import choice
print('Sorteio de nome')
a1 = input('Primeiro nome: ')
a2 = input('Segundo nome: ')
a3 = input('Terceiro nome: ')
a4 = input('Quarto Aluno: ')
lista = [a1,a2,a3,a4]

print(f'O aluno escolhido foi {choice(lista)}')