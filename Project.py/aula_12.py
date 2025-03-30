"""
Fatiamento de strings
0 1 2 3 4 5 6 7 8 9 10 11
L o r d e   S a u r o  n
------------------------------------------------------
L    o   r   d  e     S  a  u  r  o  n
-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
Fatiamento [i:f:p] [::]
     [inicio:fim:passo]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Lorde Sauron'
print(variavel[6])
print(variavel[:8])
print(variavel[2:10])
print(variavel[0:11:2])
print(variavel[-12:-1])
print(len(variavel))

#Inversão (de tras para frente)
print(variavel[::-1])
#Fatiamento [i:f:p] [::]
# [inicio:fim:passo]

#PRATICAR MAIS (FAZER VARIOS TESTES)