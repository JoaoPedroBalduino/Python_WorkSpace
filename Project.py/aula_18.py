
'''While e Break - Estrutura de repetição '''

#Repetições
#while (enquanto)
#Executa uma ação enquanto uma condição for verdadeira
#Loop infinito -> Quando um código não tem fim

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair': 
        break # o "break" procura o "while" mais proximo e 
    # finaliza o loop.

print('Acabou')

print('------------------------------------------------------------')

contador = 0 # é como se fosse o limite de repetição

while False: 
    print('teste') # ação incansavel porque a condição e "FALSE"

while contador < 10:
    contador = contador + 1
    print('teste')

print('Acabou')


print('--------------------Operadores de atribuição---------------')

#Operadores de atribuição
# =  +=  -=  *=  /=  //= **= %=

contador_1 = 0

contador_1 += 2
print(contador_1)
