print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
termos = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
t3 = t1 + t2
print('{} → {} → {} →   '.format(t1, t2, t3),end=' ')
while cont <= termos:
    cont += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print('{} →'.format(t3),end=' ')
print('FIM')
    
    
    
    

    
