print('-=' * 20)
todos = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo',
         'Botafogo', 'Bragantino', 'Fluminense', 'Athlético-PR',
         'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians',
         'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba',
         'América-MG')
print(f'LISTA DE TIMES DO BRASILEIRÃO: {todos}')
print('-=' * 20)
print(f'OS 5 PRIMEIROS SÃO {todos[0:5]}')
print('-=' * 20)
print(f'OS 4 ÚLTIMOS SÃO {todos[-4:]}')
print('-=' * 20)
print(f'TIMES EM ORDER ALFABÉTICA: {sorted(todos)}')
print('-=' * 20)
print('O FLAMENGO ESTÁ NA {} POSIÇÃO'.format(todos.index('Flamengo')+1))