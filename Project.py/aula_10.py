'''
Iterpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal(ABCDEF0123456789)
'''
preco = 1089.99
nome = 'Ricardo'
variavel = '%s o preco é R$ %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %.2f' % (1500,1500))
print('O hexadecimal de %x é %x' % (1750,1500))
# As letras são associadas repectivamente 
# as variaveis ('%s' -> nome // %f -> preco) 