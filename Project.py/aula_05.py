print("------------------------Format-----------------------")
imc = 70.0 / 1.90 ** 2
print(f'nome tem altura m de altura peso em kg')
print(f'O seu IMC é:,{imc:.2f}')
print(imc)
# Ao colocar esse "f" no começo, é abilitado a possibilidade
# do uso de variaveis nessa string
# Esse "f" significa fomat(formatação)

print("---------------------------------------------------")

a = 'Sauron'
b = 'Melkor'
c = 'Saruman'
d = 3.99

formato = 'a>{} b>{} c>{} d>{}'.format(a,b,c,d) # seguindo a ordem
formato_1 = 'a>{1} b>{0} c>{3:.3f} d>{2}'.format(a,b,c,d)
#----Pedir para exibir em 3 casas decimais------(0 1 2 3)ORDEM
formato_2 = 'a>{sa} b>{me} c>{saru} d>{num:.3f}'.format(sa=a,me=b,saru=c,num=d)

print(formato)
print(formato_1)
print(formato_2)