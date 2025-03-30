print("--------------------------------Operadores Relacionais--------------------------------------------")
'''
Operadores de comparação (relacionais)
OP------Significado------Exemplo (True)
>-------Maior------------2 > 1
>=------Maior Igual------2 >= 2
<-------Menor------------1 < 2
<=------Menor Igual------2 <= 2
==------Igual------------1 == 1 ou 'a' == 'a'
!=------Diferente--------'a' != 'a'
'''

v1 = input("Digite o valor 1: ")
v2 = input("Digite o valor 2: ") 

if v1 > v2:
    print(f'Valor de {v1=} é maior que {v2=}')
else:
    print(f'Valor de {v2=} é maior que {v1=}')