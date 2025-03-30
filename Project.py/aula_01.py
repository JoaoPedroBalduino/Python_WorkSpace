# Permite escrever um comentário
print("Senhor Sauron") #Frente
 #Frente
#Baixo

#-------------------------------------

"""
DocString
escrever uma nota entre as aspas colocadas
(Pode ser aspas simples)
"""

#-------------------------------------
print("------------sep e end---------------")
print(23, 77, 1036, sep="-",end='\n')
print(523, 123, 44, sep="-",end='\n')

# sep-> É a função para personalizar a separação.
# end-> É o que acontece no final da linha

#------------------------------------
print("-------------string--------------")
"""
Python = Liguagem de Programação
Tipo de tipagem = Dinâmica / Forte
str > string > texto
Strings são textos que estão dentro  de aspas
"""
print(123)
print("João Pedro")  #Aspas Duplas
print('João Pedro')  #Aspas Simples
print("Luiz \"Otávio\"")
# outro jeito (mais facil)
print('Luiz "Otavio"') 

#---------------------------------------
print("-------------int e float--------------")

# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é sonsiderado positivo.

print(11) #int
print(-909) #int
print(0) #int
print("---------------------------")

# float -> Número com ponto flutuante
# O tipo ou negativo com onto flutuante
# positivo ou negativo com ponto flutuante
# Float sem sinal é considerado positivo

print(1.1, 4.5)
print(0.0, -1,5)

# A função type mostra o tipo que o Python
# inferiu ao valor.

print("---------------------------")

print(type(123321))
print(type(12.1))
print(type("Eru"))
print(type("Yavanna"),type(1.0),type(2))


#-------------------------------------------
print("--------------bool-------------")

#Tipo de dado bool (boolean)
# Ao questionar algo em um programa
# Só existe duas respostas possíveis
# Sim (True) ou Não (False)
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que questiona se um valor é igual a outro.

print(10 == 10) # Sim = True (Verdadeiro)
print(10 == 5) # Não = False (Falso)
print(type(10 == 5))
print(type(True))

#-----------------------------------------
print("--------------Conv. de tipos-------------")

# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos
# str, int, float, bool 

print('1' + '2')
print('a' + 'b')
#Exeplo
print(int('1'), type(int('1')))
print(float('1.2') + 3)
print(str(11) + "b")