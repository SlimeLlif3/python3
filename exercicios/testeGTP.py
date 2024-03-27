frase = str(input('Digite uma frase: '))
a = e = i = o = u = 0
for letra in frase:
    if letra in 'aàãáAÀÃÁ':
        a += 1
    elif letra in 'eéêEÉÊ':
        e += 1
    elif letra in 'iíIÍ':
        i += 1
    elif letra in 'oôOÔ':
        o += 1
    elif letra in 'uU':
        u += 1
    
print(f'A vogal "a" aparece {a} vezes.')
print(f'A vogal "e" aparece {e} vezes.')
print(f'A vogal "i" aparece {i} vezes.')
print(f'A vogal "o" aparece {o} vezes.')
print(f'A vogal "u" aparece {u} vezes.')

 