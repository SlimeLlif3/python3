print('-=' * 20)
print('Analisador de triângulos melhorado')
print('-=' * 20)
s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmento acima PODEM FORMAR um triângulo', end=' ')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 == s2 and s1 == s3 or s2 == s1 and s3 or s3 == s1 and s2:
        print('ISÓSCELES')
    elif s1 != s2 and s3 or s3 != s1 and s2:
        print('ESCALENO')
else: 
    print('Os segmento acima NÃO PODEM FORMAR um triângulo!')





