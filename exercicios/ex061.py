print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
pa = int(input('Razão da PA: '))
termo = primeiro
c = 1

while c <= 10:
    print(termo, end=' → ' )
    c += 1
    termo += pa
print('FIM')