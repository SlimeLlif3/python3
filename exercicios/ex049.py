print(f'{" Tabuada de 10 ":=^60}')
n = int(input('Digite o número que deseja multiplicar: '))
for t in range(1,11):
    print(f'{n} x {t:2} = {n*t}')