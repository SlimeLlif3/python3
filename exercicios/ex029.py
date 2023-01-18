from termcolor import colored

vel = int(input('Qual é a velocidade atual do carro? '))

if vel >= 80 :
    mul = (vel - 80)*7
    print(colored(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${mul:.2f}','red'))

print(colored('Tenha um bom dia! Dirija com segurança!','yellow'))