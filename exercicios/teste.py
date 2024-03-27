from datetime import datetime
idade = datetime.strptime(input('Digite sua data de nascimento: '),'%Y/%m/%d')
print(f'Você nasceu no dia {idade}')