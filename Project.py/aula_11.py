"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal  + ou -
Ex. : 0>-100, .1f
Conversion flags - !r !s !a
"""
av1 = '123'
print(f'1--{av1}')
print(f'2--{av1: >10}')
print(f'3--{av1: <10}')
print(f'4--{av1: ^10}')
print(f'5--{1000.264523750294:.1f}')
print(f'6--{1000.264523750294:+,.1f}')
# ":+,.1f" Adicionar o sinal de + na frente do numero
print(f'O hexadecimal de 1500 é {1500:08X}')
#                    Pode ser - {1500:08x} para ficar minusculo 
