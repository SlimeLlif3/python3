from datetime import datetime
nasceu = int(input('Ano de nascimento: '))
atual = datetime.now().year
anos = atual - nasceu

if anos < 18:
    falta = 18 - anos
    sera = falta + atual
    print('Quem nasceu em {} tem {} anos em {}.\nAinda faltam {} anos para o alistamento militar.\nSeu alistamento será em {}.'.format(nasceu, anos, atual, falta, sera))
elif anos > 18:
    passou = anos - 18
    foi = atual - passou
    print('Quem nasceu em {} tem {} anos em {}.\nVocê já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(nasceu, anos, atual, passou, foi))
else:
    print('Quem nasceu em {} tem {} anos em {}.\nVocê se alista esse ano, boa sorte K K K.'.format(nasceu, anos, atual))
