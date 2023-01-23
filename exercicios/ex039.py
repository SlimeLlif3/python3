from datetime import date
atual = date.today().year
nasci = int(input('Ano de nascimento: '))
tenho = atual - nasci
data = (tenho-18) + atual

print(f'Quem nasceu em {nasci} tem {tenho} anos em {atual}.')

if tenho < 18:
    print(f'Ainda faltam {18-tenho} anos para o alistamento.\nSeu alistamento será em {data}. ')

elif tenho > 18:
    print(f'Você já deveria ter se alistado há {tenho-18} anos.\nSeu alistamento foi em {atual-(tenho-18)}.')

else:
    print('Você tem que se alistar IMEDIATAMENTE!')