num = int(input('Digite um número: '))
for c in range (1, num+ 1):
    if num % c == 0:
        print('\033[34m')
    else:
        print('\033[m')
    print(c, end=' ')
    