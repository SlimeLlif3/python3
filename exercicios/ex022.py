n = input('Digite seu nome completo: ')
up = n.upper()
low = n.lower()
lenth = n.__len__() - n.count(' ')
lista = n.split()


print(f"""
Analisando seu nome...
Seu nome em maiúsculas é {up}
Seu nome em minúsculas é {low}
Seu nome tem ao todo {lenth} letras
Seu primeiro nome é {lista[0]} e tem {len(lista[0])} letras 
"""
)
