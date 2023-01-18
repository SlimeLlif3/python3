name = str(input('Qual é seu nome completo? ')).upper().strip().split()
silvaIn = 'SILVA' in name
print(f'Seu nome tem Silva? {silvaIn}')