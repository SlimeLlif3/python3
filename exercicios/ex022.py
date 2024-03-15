name = str(input('Digite seu nome completo: ')).strip()
espaco = name.replace(' ','') 
separa = name.split()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
print('Seu nome tem ao todo {} letras'.format(len(espaco)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa)))