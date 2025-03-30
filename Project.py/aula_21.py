''' Iterando strings com while'''
#       0 1 2 3 4 5
Nome = 's a u r o n' # Iteráveis

#tamanho_nome = len(nome)
#print(nome)
#rint(tamanho_nome)
#print(nome[4])
#Fatiamento [i:f:p] [::]
# [inicio:fim:passo]
# # nome = J*o*a*o


nome = str(input('Digite um nome:'))
cont_len_nome = len(nome) #5

nome_2 = ' '
cont = 0
while cont < cont_len_nome:
    letra = nome[cont] 
    nome_2 += f'*{letra}'
    cont += 1

nome_2 += '*'
print (nome_2)

# OBSERVAÇÃO:
# Tive duvida na lina 20 > os "[]" é usado para indexação, 
# ou seja, acessar um caractere específico 
# dentro da string nome.