print("---------------------- Ordem  ----------------------")
# ORDEM de execução

# 1 -> ( n + n )
# 2 -> **
# 3 -> * / // %¨
# 4 -> + -

conta_1 = 1 + 1 ** 5 + 5 # objetivo que mostre 1024
print('primeira conta:',conta_1)
# A conta vai dar outro valor por conta da ordem de precedencia errada

# Jeito correto
conta_3 = (1+1) ** (5+5)
print('segunda conta:',conta_3)

print("----------------------IMC----------------------")

nome = input('Qual seu nome?:')
altura = float(input('Qual a sua altura?:'))
peso = float(input('Qual o seu peso?:'))
 
imc = peso / (altura * altura )
#imc = peso / (altura ** 2 )

print(nome,' tem',altura,'m de altura,',peso,'em kg')
print('O seu IMC é:',imc)
#print(f'O seu IMC é:,{imc:.2f}')

print("------------------------Format-----------------------")

print(f'nome tem altura m de altura peso em kg')
print(f'O seu IMC é:,{imc:.2f}')
# Ao colocar esse "f" no começo, é abilitado a possibilidade
# do uso de variaveis nessa string
# Esse "f" significa fomat(formatação)

a = 'Sauron'
b = 'Melkor'
c = 'Saruman'
d = 3000
formato = 'a>{} b>{} c>{} d>{}'.format(a,b,c,d)



