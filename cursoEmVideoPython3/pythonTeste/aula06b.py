car = input('Digite o nome de um carro: ')
print('O tipo primitivo desse valor é', type(car))
print('Só tem espaços?', car.isspace() )
print('Só tem números?', car.isnumeric())
print('Só tem letra maiúscula?', car.isupper())
print('So tem letra minúscula?', car.islower())
print('É alfabético ?', car.isalpha())
print('É um alfanum?', car.isalnum())
print('Está capitalizada ?', car.istitle())
