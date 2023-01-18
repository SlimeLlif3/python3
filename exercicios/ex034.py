s = float(input('Qual é o sálario do funcionário? R$' ))
if s <= 1250:
    porc = (s*0.15) + s
else: 
    porc = (s*0.10) + s

print(f'Quem ganhava R${s:.2f} passa a ganhar R${porc:.2f} agora.')