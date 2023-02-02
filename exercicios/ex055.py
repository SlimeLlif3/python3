maiorpeso = 0 
menorpeso = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:  
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso   
print(f'O maior peso lido foi de {maiorpeso}Kg\nO menor peso lido foi de {menorpeso}Kg')
