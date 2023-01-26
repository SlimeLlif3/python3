n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 8.0:
    print('Sua média foi excelente, meus parabéns!')
else:
    print('Sua média foi medíocre!')