# Flag (Bandeira) - Marcar um local 
# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = identidade

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

# id = codigo de identificação da variavel, possuem o 
# mesmo valor se a variavel foi igual ex: v1 = 1 e v2 = 1
# vão ter o mesmo id. 


v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2)) 